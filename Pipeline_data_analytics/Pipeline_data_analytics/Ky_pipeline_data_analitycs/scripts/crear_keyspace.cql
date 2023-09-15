-- Crea un keyspace llamado "db_casandra" con configuración simple
CREATE KEYSPACE IF NOT EXISTS db_casandra
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};
