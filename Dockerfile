# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run the FastAPI application and Celery worker
CMD ["bash", "-c", "celery -A app.celery_worker worker --loglevel=INFO & uvicorn app.main:app --host 0.0.0.0 --port 8000"]
