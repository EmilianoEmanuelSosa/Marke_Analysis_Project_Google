CREATE TABLE IF NOT EXISTS reviews (
  user_id TEXT NULL,
  restaurant_id TEXT NULL,
  stars FLOAT NULL,
  date DATE NULL,
  PRIMARY KEY (user_id, restaurant_id)
);
