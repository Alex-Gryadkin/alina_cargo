import uuid
from django.db import models
from django.contrib.auth.models import User


class Cities(models.Model):
    class City(models.TextChoices):
        ALMATY = 'ALA', 'Алматы'
        ASTANA = 'AST', 'Астана'

    city = models.CharField(
        max_length=30,
        choices=City.choices,
    )

    def __str__(self):
        return self.city


class CargoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cargouser', max_length=10)
    full_name = models.CharField(max_length=40)
    city = models.OneToOneField(Cities, on_delete=models.SET_NULL, null=True)
    cargo_code = models.CharField(max_length=15)

    def __str__(self):
        return self.user


class OTPStorage(models.Model):
    phone = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)

