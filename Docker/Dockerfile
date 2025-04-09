# Use Python 3.10 slim base image
FROM python:3.10-slim

# Prevent interactive prompts during package install
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install Tesseract OCR and system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    poppler-utils \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# (Optional) install additional language packs
# RUN apt-get update && apt-get install -y tesseract-ocr-fra

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and model
COPY app/ ./app/
COPY CNNModels/ ./CNNModels/

# Expose FastAPI default port
EXPOSE 8000

# Start FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]



