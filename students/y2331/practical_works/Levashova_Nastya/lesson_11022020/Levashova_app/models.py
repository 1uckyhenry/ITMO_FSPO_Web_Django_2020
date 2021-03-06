from django.db import models

# Create your models here.

class driver_license(models.Model):
    license_number = models.IntegerField(max_length=10)
    license_type = models.CharField(max_length=30)
    license_date = models.DateField()

class User(models.Model):
    license_number = models.ForeignKey(driver_license, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('I', 'Indefinite'),
    ])
    passport_ID = models.IntegerField(max_length=10)

class Car(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.DateField()
    state_number = models.IntegerField(max_length=20);
    cars = models.ManyToManyField(User, through='Car_User')

class Car_User(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase = models.DateField()
    sale = models.DateField()





