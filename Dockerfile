# Specify the platform to ensure compatibility
FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API script
COPY api.py .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "api.py"]