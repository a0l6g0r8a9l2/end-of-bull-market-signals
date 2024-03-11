# Use a slim Python base image for a smaller footprint
FROM python:3.9-slim

# Set the working directory for the application
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the port where your application listens
EXPOSE 8000

# Set the command to execute your application
CMD ["python", "main.py"]
