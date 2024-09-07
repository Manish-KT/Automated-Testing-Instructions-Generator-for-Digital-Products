import os
import cv2
import pytesseract
from PIL import Image
import numpy as np

class UIElementDetector:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.ui_elements = []

    def process_images(self):
        for filename in os.listdir(self.image_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(self.image_folder, filename)
                self.process_single_image(image_path)

    def process_single_image(self, image_path):
        # Read the image
        image = cv2.imread(image_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding to preprocess the image
        threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # Perform text extraction
        text = pytesseract.image_to_string(threshold)
        
        # Detect rectangles (potential buttons or input fields)
        edges = cv2.Canny(threshold, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 20 and h > 10:  # Filter out very small rectangles
                roi = threshold[y:y+h, x:x+w]
                roi_text = pytesseract.image_to_string(roi).strip()
                if roi_text:
                    element_type = self.guess_element_type(roi_text)
                    self.ui_elements.append({
                        'type': element_type,
                        'text': roi_text,
                        'position': (x, y, w, h)
                    })

    def guess_element_type(self, text):
        text = text.lower()
        if any(word in text for word in ['submit', 'login', 'sign', 'buy', 'order']):
            return 'button'
        elif any(word in text for word in ['enter', 'input', 'type']):
            return 'input field'
        elif any(word in text for word in ['select', 'choose']):
            return 'dropdown'
        elif len(text) > 50:
            return 'text area'
        else:
            return 'label'

    def get_ui_elements(self):
        return self.ui_elements

def main(image_folder):
    detector = UIElementDetector(image_folder)
    detector.process_images()
    return detector.get_ui_elements()

if __name__ == "__main__":
    # Example usage
    image_folder = "path/to/your/image/folder"
    ui_elements = main(image_folder)
    for element in ui_elements:
        print(f"Type: {element['type']}, Text: {element['text']}, Position: {element['position']}")