from django.db import models

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_price = models.IntegerField(max_length=200)
    car_link = models.URLField(max_length=200)

class Laptop(models.Model):
    laptop_name = models.CharField(max_length=50)
    laptop_price = models.IntegerField(null = True)
    laptop_link = models.URLField(max_length=200)

class Mobile(models.Model):
    mobile_name = models.CharField(max_length=50)
    mobile_price = models.IntegerField(null = True)
    mobile_link = models.URLField(max_length=200)
