FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Pillow and ffmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create uploads directory
RUN mkdir -p uploads

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port
EXPOSE 5001

# Run with gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]