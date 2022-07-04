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
        file = open('output.txt', 'w')

        image_path = input('Enter image path: ')
        print('\n\n')
        
        tess_output = ocr_pipeline.get_ocr_output(image_path)
        file.write('Tesseract output: \n')
        file.write(tess_output)
        file.write('\n\n')

        k = input('Enter k: ')
        print('\n\n')

        words, masked_doc, indices = ocr_pipeline.mask_document()
        print(" ".join(words))
        file.write('Google spell checked: \n')
        file.write(' '.join(words))
        file.write('\n\n')

        file.write('Masked output: \n')
        file.write(masked_doc)
        file.write('\n\n')

        predictions = ocr_pipeline.correct_document(int(k), masked_doc)
        final_text = ocr_pipeline.post_corr.final_text(words, indices, predictions)
        file.write('After Bert: \n')
        file.write(final_text)
        file.close()

        choice = input('Enter to continue...')
        if choice == exit:
            run = False