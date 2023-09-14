# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en /app/server
WORKDIR /app/server

# Copia el contenido de tu proyecto al directorio de trabajo
COPY . .

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y postgresql postgresql-contrib postgis

# Instala las dependencias de GDAL
RUN apt-get update && apt-get install -y \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python especificadas en requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
