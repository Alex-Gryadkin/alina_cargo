from django.db import models
from django.contrib.auth.models import User


class Cities(models.Model):
    city_name = models.CharField(max_length=30, null=True)
    city_short_name = models.CharField(max_length=5, null=True)

    class Meta:
        verbose_name_plural = 'Города'
    def __str__(self):
        return str(self.city_name)

class CargoUser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cargouser', max_length=10)
    full_name = models.CharField(max_length=40, unique=False)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    cargo_code = models.CharField(max_length=15)
    is_activated = models.BooleanField(default=True, verbose_name='Активен')


    def __str__(self):
        return str(self.username)

    def get_last_login(self):
        last_login = self.username.last_login
        return last_login


class OTPStorage(models.Model):
    phone = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


