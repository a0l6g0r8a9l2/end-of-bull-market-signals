# Use a slim Python base image for a smaller footprint
FROM python:3.9-slim

# Set the working directory for the application
WORKDIR /src

# No binary .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# For pretty prints
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt
COPY requirements.txt requirements.txt 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app app

# Set the command to execute your application
# CMD ["python", "main.py"]
