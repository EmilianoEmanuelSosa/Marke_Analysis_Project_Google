from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review_count = models.IntegerField()
    categories = models.CharField(max_length=512)


class User(models.Model):
    user_id = models.CharField(max_length=512, primary_key=True)
    name = models.CharField(max_length=512)


class Review(models.Model):
    user_id = models.CharField(max_length=512)
    restaurant_id = models.CharField(max_length=512)
    stars = models.DecimalField(max_digits=3, decimal_places=1)
    text = models.TextField()
    date = models.DateField()
