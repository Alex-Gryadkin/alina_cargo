import uuid
from django.db import models
from django.contrib.auth.models import User


class Cities(models.Model):
    class Meta:
        verbose_name_plural = 'Города'
    class City(models.TextChoices):  # refacrtor this part

        ALMATY = 'ALA', 'Алматы'
        ASTANA = 'AST', 'Астана'

    city = models.CharField(
        max_length=30,
        choices=City.choices,
    )

    def __str__(self):
        return self.city


class CargoUser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cargouser', max_length=10)
    full_name = models.CharField(max_length=40, unique=False)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    cargo_code = models.CharField(max_length=15)
    is_activated = models.BooleanField(default=False)

    USERNAME_FIELD = "user"

    def __str__(self):
        return self.username


class OTPStorage(models.Model):
    phone = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


