from rest_framework import serializers
from .models import Restaurant, Review,User

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = '_all_'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '_all_'