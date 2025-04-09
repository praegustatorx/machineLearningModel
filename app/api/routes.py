from fastapi import APIRouter, File, UploadFile
from app.services.image_utils import preprocess_image
from app.services.model_loader import model
from app.core.config import class_names
import numpy as np
from PIL import Image
import pytesseract
import io

router = APIRouter()

@router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        img_array = preprocess_image(image_bytes)

        predictions = model.predict(img_array)[0]
        predicted_index = int(np.argmax(predictions))
        predicted_label = class_names[predicted_index]
        confidence = float(predictions[predicted_index])

        return {"predicted_class": predicted_label, "confidence": confidence}
    except Exception as e:
        return {"error": str(e)}


@router.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Perform OCR using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        return {"extracted_text": extracted_text}
    except Exception as e:
        return {"error": str(e)}