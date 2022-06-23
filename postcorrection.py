import torch
from transformers import pipeline

class PostCorrection():
    def __init__(self) -> None:
        self.pipeline = pipeline("fill-mask", model="urduhack/roberta-urdu-small", tokenizer="urduhack/roberta-urdu-small")
        self.model = self.pipeline.model
        self.tokenizer = self.pipeline.tokenizer
        self.doc = None
        self.predictions = []

    def apply_correction(self, doc):
        self.doc = doc

        inputs = self.tokenizer(self.doc, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits

        # retrieve mask indices
        mask_token_index = (inputs.input_ids == self.tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

        # get indices of top k max probability tokens
        top_k_tokens = logits[0, mask_token_index].topk(k=10, dim=1).indices

        # record predictions for each mask
        for i in top_k_tokens:
            self.predictions.append(self.tokenizer.decode(i))

        return self.predictions