#!/bin/bash

# Inicia PostgreSQL en segundo plano
service postgresql start &

# Espera hasta que PostgreSQL esté disponible (se verifica si se puede conectar)
while ! pg_isready -q -h localhost -U $POSTGRES_USER -d $POSTGRES_DB; do
  echo "Esperando a que PostgreSQL se inicie..."
  sleep 5
done

echo "----------------------"
echo "PostgreSQL iniciado y disponible."

# Ejecuta el script SQL para crear la base de datos
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f '/scripts/consultas.sql'

echo "Creando la base de datos..."
echo "----------------------"

# Mantén el contenedor en ejecución
tail -f /dev/null
