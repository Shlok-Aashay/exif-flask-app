FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies for Pillow and ffmpeg
RUN apk update && apk add --no-cache \
    ffmpeg \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    libjpeg-turbo-utils \
    libpng-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    gcc \
    g++ \
    musl-dev \
    libffi-dev \
    python3-dev \
    build-base \
    && pip install --upgrade pip

COPY requirements.txt /app/

# Only use pre-built wheels to avoid setup.py issues
RUN pip install --only-binary=:all: -r requirements.txt

COPY . /app/

RUN mkdir -p uploads

EXPOSE 5001

CMD ["python", "app.py"]
