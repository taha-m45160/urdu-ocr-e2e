from numpy import indices
import tesseract
import mask
import postcorrection
import os
import sys

class Pipeline:
    def __init__(self) -> None:
        self.image = None
        self.doc = ""
        self.ocr_engine = tesseract.OCR('UrduNastaleeq')
        self.masking_engine = mask.MaskingEngine()
        self.post_corr = postcorrection.PostCorrection()

    def get_ocr_output(self, image_path):
        """
        retrieve output from OCR engine
        """

        # self.doc = input('Enter line: ')
        self.doc = self.ocr_engine.detect_text(image_path)

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

    run = True
    while run:
        os.system('clear')

        try:
            image_path = sys.argv[1]
        except:
            print('Image path not found.')
            sys.exit()
        
        tess_output = ocr_pipeline.get_ocr_output(image_path)
        print(tess_output)

        print('\n\n')

        k = input('Enter k: ')
        words, masked_doc, indices = ocr_pipeline.mask_document()

        print('\n\n')
        predictions = ocr_pipeline.correct_document(int(k), masked_doc)
        
        final_text = ocr_pipeline.post_corr.final_text(words, indices, predictions)

        print(final_text)

        choice = input('\n')

        if choice == exit:
            run = False