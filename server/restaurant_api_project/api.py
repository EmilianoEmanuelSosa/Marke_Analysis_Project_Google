from rest_framework import viewsets, permissions
from .models import Restaurant, Review, User
from .serializers import RestaurantSerializer, ReviewSerializer,UserSerializer
from rest_framework.response import Response

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RestaurantSerializer
    lookup_field = 'restaurant_id'

    def retrieve(self, request, restaurant_id=None):
        try:
            restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
            serializer = self.get_serializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({'message': 'El restaurante no existe.'}, status=404)

    def get_restaurants_in_radius(self, request, restaurant_id=None, radius_km=None):
        try:
            # Obtén el restaurante de referencia
            reference_restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
            reference_latitude = reference_restaurant.latitude
            reference_longitude = reference_restaurant.longitude

            # Calcula la distancia máxima y mínima para buscar restaurantes dentro del radio
            max_distance = radius_km
            min_distance = 0

            # Filtra los restaurantes en el radio especificado
            restaurants_in_radius = Restaurant.objects.filter(
                latitude__range=(reference_latitude - max_distance, reference_latitude + max_distance),
                longitude__range=(reference_longitude - max_distance, reference_longitude + max_distance),
            )

            serializer = self.get_serializer(restaurants_in_radius, many=True)
            return Response(serializer.data)

        except Restaurant.DoesNotExist:
            return Response({'message': 'El restaurante no existe.'}, status=404)

    def get_reviews_for_restaurant(self, request, restaurant_id=None):
        try:
            # Obtén el restaurante
            restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)

            # Obtén todas las reseñas relacionadas con ese restaurante
            reviews = Review.objects.filter(restaurant=restaurant)

            # Serializa las reseñas
            serializer = ReviewSerializer(reviews, many=True)

            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({'message': 'El restaurante no existe.'}, status=404)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    lookup_field = 'user_id'  # Campo de búsqueda personalizado

    def retrieve(self, request, user_id=None):
        try:
            user = User.objects.get(user_id=user_id)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'El usuario no existe.'}, status=404)