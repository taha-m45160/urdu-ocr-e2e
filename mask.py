class MaskingEngine():
    def __init__(self) -> None:
        with open('dictionary/words.txt') as ur:
            temp = ur.read().strip().split('\n')
        self.urd_dict = set(temp)


    def mask(self, doc):
        words = doc.split(' ')
        masked = []
        indices = []
        for idx, word in enumerate(words):            
            if word in self.urd_dict:
                masked.append(word)
            else:
                indices.append(idx)
                masked.append('<mask>')

        masked_doc = ' '.join(masked)

        return words, masked_doc, indices