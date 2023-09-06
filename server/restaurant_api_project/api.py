from rest_framework import viewsets, permissions
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework.response import Response

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RestaurantSerializer
    lookup_field = 'restaurant_id'  # Campo de búsqueda personalizado

    def retrieve(self, request, restaurant_id=None):
        try:
            restaurant = Restaurant.objects.get(restaurant_id=restaurant_id)
            serializer = self.get_serializer(restaurant)
            return Response(serializer.data)
        except Restaurant.DoesNotExist:
            return Response({'message': 'El restaurante no existe.'}, status=404)