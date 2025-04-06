import tensorflow as tf
import os

model_path = os.path.join("CNNModels", "IngredientClassifier.h5")
model = tf.keras.models.load_model(model_path)
