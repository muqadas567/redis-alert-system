# Base image Python ka use karenge
FROM python:3.10-slim

# Working directory set karein
WORKDIR /app

# Dependencies copy aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki saara code copy karein
COPY app.py .

# Script ko run karne ki command
CMD ["python", "app.py"]