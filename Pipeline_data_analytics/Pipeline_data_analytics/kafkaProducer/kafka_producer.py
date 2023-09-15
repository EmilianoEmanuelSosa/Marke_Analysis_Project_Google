from kafka import KafkaProducer
from cassandra.cluster import Cluster

# Configuración de Kafka
producer = KafkaProducer(bootstrap_servers='kafka:9092')

# Configuración de Cassandra
cluster = Cluster(['cassandra'])
session = cluster.connect('db_casandra')

# Consulta de ejemplo en Cassandra para seleccionar los primeros 5000 registros
query = "SELECT * FROM reviews LIMIT 5000"
rows = session.execute(query)

# Envía cada fila a Kafka
for row in rows:
    producer.send('db_casandra', str(row).encode('utf-8'))

# Cierra las conexiones
producer.close()
session.shutdown()
cluster.shutdown()
