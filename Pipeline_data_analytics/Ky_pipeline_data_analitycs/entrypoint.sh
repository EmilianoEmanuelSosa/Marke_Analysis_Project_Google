#!/bin/bash

# Inicia Cassandra en segundo plano
cassandra -R &
cassandra_pid=$!

echo "Iniciando Cassandra..."

# Espera hasta que Cassandra esté disponible (se verifica si se puede conectar)
while ! cqlsh -e "SHOW HOST" 2>/dev/null; do
  echo "Esperando a que Cassandra se inicie..."
  sleep 5
done
echo "----------------------"
echo "Cassandra iniciada y disponible."

# Ejecuta el script CQL para crear el keyspace en segundo plano
cqlsh -f '/Ky_pipeline_data_analitycs/scripts/crear_keyspace.cql' &

echo "Creando el keyspace..."
echo "----------------------"
# Espera un momento antes de seleccionar el keyspace y crear la tabla
sleep 10

# Selecciona el keyspace
cqlsh -e "USE mikeyspace;"

echo "Usando el keyspace 'mikeyspace'."
echo "----------------------"
# Ejecuta el script CQL para crear la tabla en segundo plano
cqlsh -f '/Ky_pipeline_data_analitycs/scripts/consultas.cql' &

echo "Creando la tabla..."
echo "----------------------"
echo "Lista la tabla.."
# Mantén el contenedor en ejecución
tail -f /dev/null
