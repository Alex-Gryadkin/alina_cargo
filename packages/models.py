from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Packages(models.Model):
    class Meta:
        verbose_name_plural = 'Трек-номера'
    id = models.CharField(
        max_length=50,
        primary_key=True,
        verbose_name='Трек'
    )
    status_choices = [
        ('new', '📝 Добавлен'),
        ('eha', '🚚 В пути'),
        ('tut', '🗿 Ожидает'),
        ('vse', '🤝 Выдан')
    ]
    status = models.CharField(
        max_length = 3,
        choices = status_choices,
        default = 'new',
        verbose_name = 'Статус'
    )
    status_change_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.status_change_date = datetime.now()
        super().save(*args, **kwargs)

class UserPackages(models.Model):
    class Meta:
        verbose_name_plural = 'Трек-номера пользователей'
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    package_id = models.ForeignKey(Packages, default=None, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50)
    def __str__(self):
        return str(self.user_id)+' : '+str(self.package_id)
