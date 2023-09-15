-- Crea la tabla "reviews" en el keyspace "db_casandra"
CREATE TABLE IF NOT EXISTS db_casandra.reviews (
  user_id TEXT,
  restaurant_id TEXT,
  stars FLOAT,
  date DATE,
  PRIMARY KEY (user_id, restaurant_id)
);
