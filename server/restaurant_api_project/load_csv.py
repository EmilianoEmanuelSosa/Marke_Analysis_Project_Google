import csv
from decimal import Decimal
from .models import Restaurant, User, Review
from datetime import date
from django.db import IntegrityError

# Rutas a los archivos CSV
csv_file_path_restaurants = '/home/mkm/programin/Marke_Analysis_Project_Google/Data/Data_process/restaurants.csv'


def import_restaurants_from_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        restaurants_to_create = []

        for row in csv_reader:
            # Asegúrate de que los nombres de las columnas coincidan con los del CSV
            restaurant_id = row['restaurant_id']

            try:
                restaurant, created = Restaurant.objects.get_or_create(
                    restaurant_id=restaurant_id,
                    defaults={
                        'name': row['name'],
                        'address': row['address'],
                        'latitude': Decimal(row['latitude']),
                        'longitude': Decimal(row['longitude']),
                        'rating': Decimal(row['rating']),
                        'review_count': int(row['review_count']),
                        'categories': row['categories']
                    }
                )

                if created:
                    restaurants_to_create.append(restaurant)

                if len(restaurants_to_create) == BATCH_SIZE:
                    Restaurant.objects.bulk_create(restaurants_to_create)
                    restaurants_to_create = []

            except IntegrityError:
                # Ignorar registros duplicados
                pass

        # Inserta cualquier remanente que quede en el último lote
        if restaurants_to_create:
            Restaurant.objects.bulk_create(restaurants_to_create)

















def import_reviews_from_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        reviews_to_create = []

        for row in csv_reader:
            # Asegúrate de que los nombres de las columnas coincidan con los del CSV
            user_id = row['user_id']
            restaurant_id = row['restaurant_id']

            review = Review(
                user_id=user_id,
                restaurant_id=restaurant_id,
                stars=Decimal(row['stars']),
                text=row['text'],
                date=date.fromisoformat(row['date'])  # Asume que la fecha está en formato ISO
            )
            reviews_to_create.append(review)

            if len(reviews_to_create) == BATCH_SIZE:
                Review.objects.bulk_create(reviews_to_create)
                reviews_to_create = []

        # Inserta cualquier remanente que quede en el último lote
        if reviews_to_create:
            Review.objects.bulk_create(reviews_to_create)



















def import_users_from_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        users_to_create = []

        for row in csv_reader:
            # Asegúrate de que los nombres de las columnas coincidan con los del CSV
            user = User(
                user_id=row['user_id'],
                name=row['name']
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