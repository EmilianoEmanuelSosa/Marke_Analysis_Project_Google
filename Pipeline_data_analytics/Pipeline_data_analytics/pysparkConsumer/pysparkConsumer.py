from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_date, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import psycopg2
from decouple import config

# Configura la sesión de Spark
spark = SparkSession.builder \
    .appName("KafkaPySparkConsumer") \
    .getOrCreate()

# Define el esquema para los datos JSON que se consumirán de Kafka
schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("restaurant_id", StringType(), True),
    StructField("stars", StringType(), True),
    StructField("date", StringType(), True)
])

# Configura la fuente de Kafka
kafka_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "db_casandra") \
    .load()

# Convierte los datos en formato JSON y aplica el esquema
kafka_json_df = kafka_df \
    .selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Agrega el campo de fecha y hora actual
kafka_json_df = kafka_json_df.withColumn("date", to_date("date", "dd-MM-yy"))
kafka_json_df = kafka_json_df.withColumn("stars", kafka_json_df["stars"].cast(IntegerType()))
kafka_json_df = kafka_json_df.withColumn("timestamp", current_timestamp())

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database=config(POSTGRES_DB),
    user=config(POSTGRES_USER),
    password=config(POSTGRES_PASSWORD)
)

# Escribe los datos en la tabla deseada
kafka_json_df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/db_postgres") \
    .option("dbtable", "nombre_de_la_tabla") \
    .option("user", "tu_usuario") \
    .option("password", "tu_contraseña") \
    .save()

# Inicia la consulta de Spark en tiempo real
query = kafka_json_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
