from PIL import Image
import pytesseract
import re
import io

def extract_text_and_date(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes))

    # Perform OCR using pytesseract
    extracted_text = pytesseract.image_to_string(image)

    # Extract dates using regex
    date_pattern = r'\b(?:\d{1,4}[-./\s]){2}\d{1,4}\b'
    found_dates = re.findall(date_pattern, extracted_text)

    return found_dates[0] if found_dates else ""
