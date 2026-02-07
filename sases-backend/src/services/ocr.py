from typing import List
import cv2
import easyocr

class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, image_path: str) -> List[str]:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to load.")
        
        results = self.reader.readtext(image)
        extracted_texts = [result[1] for result in results]
        return extracted_texts

    def extract_text_from_roi(self, image_path: str, roi: tuple) -> str:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to load.")
        
        x_start, y_start, x_end, y_end = roi
        cropped_image = image[y_start:y_end, x_start:x_end]
        results = self.reader.readtext(cropped_image)
        
        if results:
            return results[0][1]
        return ""