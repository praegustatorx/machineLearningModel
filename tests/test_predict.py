import pytest
from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_predict_with_valid_image():
    image_path = os.path.join("tests", "test_images", "eggs.jpg_3.jpeg")  # Make sure this image exists

    with open(image_path, "rb") as image_file:
        response = client.post(
            "/predict/",
            files={"file": ("butter.jpg", image_file, "image/jpeg")}
        )

    assert response.status_code == 200
    result = response.json()
    assert "predicted_class" in result
    assert "confidence" in result
    assert isinstance(result["confidence"], float)

def test_predict_with_invalid_file():
    response = client.post(
        "/predict/",
        files={"file": ("fake.txt", b"not an image", "text/plain")}
    )

    assert response.status_code == 200
    assert "error" in response.json()

