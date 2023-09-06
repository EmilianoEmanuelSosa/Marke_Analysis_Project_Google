from django.urls import path, re_path
from .api import RestaurantViewSet

urlpatterns = [
    path('restaurantes_id/<str:restaurant_id>/', RestaurantViewSet.as_view({'get': 'retrieve'}), name='restaurant-detail'),
]
