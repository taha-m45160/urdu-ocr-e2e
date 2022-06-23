import mask
import tesseract

class Pipeline:
    def __init__(self) -> None:
        self.image = None
        self.doc = "My name is Taha. I am part of the CSaLT fam. We are making an OCR"
        self.ocr_engine = tesseract.OCR()
        self.masking_engine = mask.MaskingEngine()


    def get_ocr_output(self):
        """
        retrieve output from OCR engine
        """
        pass

    def split_document(self):
        """
        split ocr output into sentences/(phrases?)

        input: ocr output document
        return: array of sentences in the original document 
        """
        return self.doc.split('.')

    def maskDocument():
        """
        mask each sentence as appropriate
        """
        pass

    def correctDocument():
        """
        correct the masked ocr output
        """
        pass

    def joinDocument():
        """
        join sentences/phrases(?) to form coherent document
        """
        pass

potentialDrawbacks = """
    -> too many masks in one input
    -> incorrect names
    -> incorrectly joined words due to omitted space
"""

# # retrieve output from OCR engine
# # we will call this output a document
# ocr_output = getOCROutput()

# # split document into sentences/(phrases?)
# split_doc = split_document(ocr_output)

# # mask each sentence as appropriate
# masked_doc = maskDocument(split_doc)

# # feed each sentence as input to post-correction model
#     # get the top k predictions for each mask in a sentence
#     # compare each of the k predictions with the masked output to obtain matched_character_count
#     # select prediction with highest matched_character_count and replace
# corrected_doc = correctDocument()

# # join output as necessary to form a new document
# final_doc = joinDocument()

if __name__ == '__main__':
    ocr_pipeline = Pipeline()

    print(ocr_pipeline.split_document())