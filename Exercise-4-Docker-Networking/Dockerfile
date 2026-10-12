# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5001

# Start the application
CMD ["python", "app.py"]