/copy  restaurant_api_project_user(name,user_id)
FROM '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/users.csv'
DELIMITER ',' CSV HEADER;


\copy restaurant_api_project_restaurant(restaurant_id, name, address, latitude, longitude, rating, review_count, categories)
FROM '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/restaurants.csv' DELIMITER ',' CSV HEADER;

\copy restaurant_api_project_review(user_id, restaurant_id, rating, text, time)
FROM '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/reviews.csv' DELIMITER ',' CSV HEADER;