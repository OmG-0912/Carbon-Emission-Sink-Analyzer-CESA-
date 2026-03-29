import cv2
import pytesseract
from PIL import Image

# If Windows, specify path to tesseract.exe
# Uncomment and update if needed:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    # Read image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to improve OCR accuracy
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Optional: Resize image for better accuracy
    resized = cv2.resize(thresh, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    # Convert to PIL Image
    pil_img = Image.fromarray(resized)

    # Extract text
    text = pytesseract.image_to_string(pil_img, config='--psm 6')

    return text


if __name__ == "__main__":
    image_path = "Prescription9.jpg"  # Replace with your image path
    extracted_text = extract_text_from_image(image_path)

    print("\nExtracted Prescription Text:\n")
    print(extracted_text)
