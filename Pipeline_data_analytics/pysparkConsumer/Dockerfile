# Usar una imagen de Python
FROM python:3.9

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar las dependencias de Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el script del consumidor PySpark
COPY pyspark_consumer.py .

# Ejecutar el script del consumidor PySpark
CMD ["python", "pyspark_consumer.py"]
