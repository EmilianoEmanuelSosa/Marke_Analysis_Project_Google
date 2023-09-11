from django.urls import path, re_path
from .api import RestaurantViewSet,UserViewSet

urlpatterns = [
    # Otras rutas...
    path('restaurantes_id/<str:restaurant_id>/', RestaurantViewSet.as_view({'get': 'retrieve'}), name='restaurant-detail'),
    path('restaurantes_en_radio/<str:restaurant_id>/<int:radius_km>/', RestaurantViewSet.as_view({'get': 'get_restaurants_in_radius'}), name='restaurants-in-radius'),
    path('restaurantes_reviews/<str:restaurant_id>/', RestaurantViewSet.as_view({'get': 'get_reviews_for_restaurant'}), name='restaurant-reviews'),
    path('usuarios/<str:user_id>/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail')

]