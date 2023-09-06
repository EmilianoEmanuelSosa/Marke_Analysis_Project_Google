from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=512)
    class Meta:
        indexes = [
            models.Index(fields=['user_id'])
        ]

class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review_count = models.IntegerField()
    categories = models.CharField(max_length=512)
    class Meta:
        indexes = [
            models.Index(fields=['restaurant_id'])
        ]

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    time = models.DateField()



