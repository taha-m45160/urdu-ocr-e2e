from numpy import argmin
import re
import torch
from transformers import pipeline
import enchant
  
class PostCorrection():
    def __init__(self) -> None:
        self.pipeline = pipeline("fill-mask", model="urduhack/roberta-urdu-small", tokenizer="urduhack/roberta-urdu-small")
        self.model = self.pipeline.model
        self.tokenizer = self.pipeline.tokenizer
        self.doc = None
        self.predictions = []

    def metric(self, word, pred):
        return enchant.utils.levenshtein(word, pred)

    def best_match(self, word, predictions):
        similarity_score = []
        
        for pred in predictions:
            similarity_score.append(self.metric(word, pred))
        
        return predictions[argmin(similarity_score)]

    def final_text(self, words, indices, predictions):
        for i, idx in enumerate(indices):
            word = words[idx]
            pred = predictions[i]
            match = self.best_match(word, pred)
            words[idx] = match
        
        return ' '.join(words)

    def apply_correction(self, k, doc):
        self.doc = doc

        inputs = self.tokenizer(self.doc, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits

        # retrieve mask indices
        mask_token_index = (inputs.input_ids == self.tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

        # get indices of top k max probability tokens
        top_k_tokens = logits[0, mask_token_index].topk(k=k, dim=1).indices
        
        self.predictions = []
        # record predictions for each mask
        for i in top_k_tokens:
            self.predictions.append(self.tokenizer.decode(i))

        return self.predictions