# import pandas as pd
# from decimal import Decimal
# from .models import Restaurant, User, Review
# from datetime import date
# from django.db import IntegrityError

# # Rutas a los archivos CSV
# csv_file_path_restaurants = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/restaurants.csv'
# csv_file_path_reviews = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/reviews.csv'
# csv_file_path_users = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/users.csv'

# BATCH_SIZE = 10000



# def import_restaurants_from_csv(file_path):
#     df = pd.read_csv(file_path)
#     reviews_to_create = []
#         for row in csv_reader:
#             # Asegúrate de que los nombres de las columnas coincidan con los del CSV
#             restaurant_id = row['restaurant_id']
#             name = row['name']
#             address = row['address']
#             latitude = float(row['latitude'])
#             longitude = float(row['longitude'])
#             rating = Decimal(row['rating'])
#             review_count = int(row['review_count'])
#             categories = row['categories']

#             # Crea una instancia del modelo Restaurant con los datos del CSV
#             restaurant = Restaurant(

#             )

#             restaurants_to_create.append(restaurant)

#             if len(restaurants_to_create) == BATCH_SIZE:
#                 # Inserta los restaurantes en lotes
#                 Restaurant.objects.bulk_create(restaurants_to_create)
#                 restaurants_to_create = []

#         # Inserta cualquier remanente que quede en el último lote
#         if restaurants_to_create:
#             Restaurant.objects.bulk_create(restaurants_to_create)



# def import_reviews_from_csv(file_path):
#     df = pd.read_csv(file_path)
#     reviews_to_create = []

#     for index, row in df.iterrows():
#         user_id = row['user_id']
#         restaurant_id = row['restaurant_id']
#         rating = Decimal(row['stars'])
#         # Asume que 'date' está en formato ISO (YYYY-MM-DD)
#         time = date.fromisoformat(row['date'])
#         text = row['text']

#         # Crea el objeto Review y agrégalo a la lista
#         review = Review(
#             user_id=user_id,
#             restaurant_id=restaurant_id,
#             rating=rating,
#             text=text,
#             time=time
#         )
#         reviews_to_create.append(review)

#         if len(reviews_to_create) == BATCH_SIZE:
#             Review.objects.bulk_create(reviews_to_create)
#             reviews_to_create = []

#     if reviews_to_create:
#         Review.objects.bulk_create(reviews_to_create)



# def import_users_from_csv(file_path):
#     with open(file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         users_to_create = []

#         for row in csv_reader:
#             # Asegúrate de que los nombres de las columnas coincidan con los del CSV
#             user = User(
#                 user_id=row['user_id'],
#                 name=row['name']
#             )
#             users_to_create.append(user)

#             if len(users_to_create) == BATCH_SIZE:
#                 User.objects.bulk_create(users_to_create)
#                 users_to_create = []

#         # Inserta cualquier remanente que quede en el último lote
#         if users_to_create:
#             User.objects.bulk_create(users_to_create)




# import_reviews_from_csv(csv_file_path_reviews)

