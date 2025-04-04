from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import io
import numpy as np
from PIL import Image
import os

# Initialize FastAPI app
app = FastAPI()

class_names = ['Butter', 'Eggs', 'PackagedBread']

# Load the model once when the server starts
model_path = os.path.join("CNNModels", "IngredientClassifier.h5")
model = tf.keras.models.load_model(model_path)

# Preprocessing function
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((128, 128))  # Resize to match model input
    img_array = np.array(image) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        img_array = preprocess_image(image_bytes)

        predictions = model.predict(img_array)[0]  # Get the prediction array
        predicted_index = int(np.argmax(predictions))  # Get highest probability index
        predicted_label = class_names[predicted_index]  # Get class name
        confidence = float(predictions[predicted_index])  # Get confidence score

        return {"predicted_class": predicted_label, "confidence": confidence}
    except Exception as e:
        return {"error": str(e)}

# Run the API with: uvicorn server:app --reload
