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

    def __str__(self):  # to show title (string) not an 'object' in admin section and while interactions
        return self.city


class CargoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    cargo_code = models.CharField(max_length=15)

    def __str__(self):
        return self.user
