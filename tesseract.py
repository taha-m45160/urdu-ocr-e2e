import pytesseract
import cv2

class OCR:
    def __init__(self, model) -> None:
        self.model = model

    def detect_text(self, image_path):
        image = cv2.imread(image_path)
        response = pytesseract.image_to_string(image, lang=self.model, config='--psm 11')
        return response