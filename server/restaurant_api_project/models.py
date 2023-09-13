from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=512, null=True)  # Permite valores nulos en el campo 'name'
    class Meta:
        indexes = [
            models.Index(fields=['user_id'])
        ]

class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=512,null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    review_count = models.IntegerField(null=True)
    categories = models.CharField(max_length=512,null=True)
    class Meta:
        indexes = [
            models.Index(fields=['restaurant_id'])
        ]

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.FloatField(null=True)
    text = models.TextField(null=True)
    time = models.DateField(null=True)



