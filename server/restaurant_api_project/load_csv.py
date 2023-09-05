from .models import Restaurant, User, Review
import csv
from decimal import Decimal
from django.utils.dateparse import parse_date

# Rutas a los archivos CSV
csv_file_path_restaurants = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/restaurants.csv'
csv_file_path_reviews = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/reviews.csv'
csv_file_path_users = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/users.csv'

def import_restaurants_from_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        restaurants_to_create = []

        for row in csv_reader:
            restaurant = Restaurant(
                name=row['name'],
                address=row['address'],
                latitude=Decimal(row['latitude']),
                longitude=Decimal(row['longitude']),
                rating=Decimal(row['rating']),
                review_count=int(row['review_count']),
                categories=row['categories']
            )
            restaurants_to_create.append(restaurant)

            if len(restaurants_to_create) == BATCH_SIZE:
                Restaurant.objects.bulk_create(restaurants_to_create)
                restaurants_to_create = []

        # Inserta cualquier remanente que quede en el último lote
        if restaurants_to_create:
            Restaurant.objects.bulk_create(restaurants_to_create)



def import_reviews_from_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        reviews_to_create = []

        for row in csv_reader:
            user_id = row['user_id']  # Mantén user_id como cadena
            restaurant_id = row['restaurant_id']  # Mantén restaurant_id como cadena

            # No es necesario verificar si el usuario o el restaurante existen previamente

            review = Review(
                user_id=user_id,
                restaurant_id=restaurant_id,
                stars=Decimal(row['stars']),  # Utiliza 'stars' en lugar de 'rating'
                text=row['text'],
                date=parse_date(row['date'])  # Utiliza 'date' en lugar de 'time'
            )
            reviews_to_create.append(review)

            if len(reviews_to_create) == BATCH_SIZE:
                Review.objects.bulk_create(reviews_to_create)
                reviews_to_create = []

        # Inserta cualquier remanente que quede en el último lote
        if reviews_to_create:
            Review.objects.bulk_create(reviews_to_create)

# Llama a la función para importar las revisiones desde el archivo CSV
import_reviews_from_csv(csv_file_path_reviews)

def import_users_from_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        users_to_create = []

        for row in csv_reader:
            user = User(
                name=row['name'],
                registration_date=parse_date(row['registration_date'])
            )
            users_to_create.append(user)

            if len(users_to_create) == BATCH_SIZE:
                User.objects.bulk_create(users_to_create)
                users_to_create = []

        # Inserta cualquier remanente que quede en el último lote
        if users_to_create:
            User.objects.bulk_create(users_to_create)

BATCH_SIZE = 3000  # Ajusta el tamaño del lote según tus necesidades

# Llama a las funciones para importar datos desde los archivos CSV
import_restaurants_from_csv(csv_file_path_restaurants)
import_reviews_from_csv(csv_file_path_reviews)
import_users_from_csv(csv_file_path_users)
