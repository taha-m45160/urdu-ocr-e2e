from numpy import indices
import tesseract
import mask
import postcorrection
import os

class Pipeline:
    def __init__(self) -> None:
        self.image = None
        self.doc = ""
        self.ocr_engine = tesseract.OCR()
        self.masking_engine = mask.MaskingEngine()
        self.post_corr = postcorrection.PostCorrection()

    def get_ocr_output(self):
        """
        retrieve output from OCR engine
        """
        # with open('sample_gt/1.txt') as gt:
        #     self.doc = gt.read().replace('\n', '')[:-1]

        line = input('Enter line: ')
        self.doc = line

        return self.doc

    def mask_document(self):
        """
        mask each sentence as appropriate
        """
        return self.masking_engine.mask(self.doc)

    def correct_document(self, k, masked_doc):
        """
        correct the masked ocr output
        """

        final = self.post_corr.apply_correction(k, masked_doc)

        final_output = []
        for pred in final:
            temp = pred.strip().split(' ')
            final_output.append(temp)

        return final_output

if __name__ == '__main__':
    ocr_pipeline = Pipeline()

    # ocr_pipeline.get_ocr_output()
    # with open('sample_gt/1_masked.txt') as gt:
    #     doc = gt.read()

    # masked_doc = ocr_pipeline.mask_document()

    # corrected_doc = ocr_pipeline.correct_document(doc)

    # print(corrected_doc)

    run = True
    while run:
        os.system('clear')
        
        ocr_pipeline.get_ocr_output()
        k = input('Enter k: ')
        words, masked_doc, indices, masked = ocr_pipeline.mask_document()
        print('\n\n')
        print('Masked: ', masked_doc)
        print(masked)
        print(words)
        print('\n\n')
        corrected_line = ocr_pipeline.correct_document(int(k), masked_doc)
        for cl in corrected_line:
            print(cl)
        choice = input('\n')
        if choice == exit:
            run = False

    
