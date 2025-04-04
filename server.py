from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Initialize FastAPI app
app = FastAPI()

# Load the model once when the server starts
model = tf.keras.models.load_model("IngredientClassifier.h5")  # Make sure your model is in the 'model' directory

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
        # Read file bytes and preprocess image
        image_bytes = await file.read()
        img_array = preprocess_image(image_bytes)

        # Make prediction
        predictions = model.predict(img_array)
        predicted_class = int(np.argmax(predictions[0]))  # Get class index

        return {"predicted_class": predicted_class}
    except Exception as e:
        return {"error": str(e)}

# Run the API with: uvicorn server:app --reload
