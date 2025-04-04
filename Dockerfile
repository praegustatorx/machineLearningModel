# Use Python 3.10 as a slim base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY server.py /app/
COPY IngredientClassifier.h5 /app/

# Expose the port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]


