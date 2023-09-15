# Usar una imagen de Python
FROM python:3.9

# Directorio de trabajo dentro del contenedor
WORKDIR /app/kafla/

# Instalar las dependencias de Python
COPY COPY requirements.txt .

RUN pip install -r requirements.txt

# Copiar el script del productor Kafka
COPY kafka_producer.py .

# Ejecutar el script del productor Kafka
CMD ["python", "kafka_producer.py"]
