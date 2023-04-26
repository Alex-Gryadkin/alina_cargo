from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    class Meta:
        verbose_name_plural = 'Статусы'
        ordering = ['order']

    code = models.CharField(max_length=3,
                            unique=True,
                            verbose_name='Код')
    name = models.CharField(max_length=20,
                            verbose_name='Название')
    bg_color = models.CharField(max_length=7,
                                verbose_name='Цвет фона',
                                )
    txt_color = models.CharField(max_length=7,
                                 verbose_name='Цвет текста',
                                 blank=True
                                 )
    order = models.IntegerField(default=0,
                                blank=False,
                                null=False,
                                )

    def __str__(self):
        return self.code


# Create your models here.
class Packages(models.Model):
    class Meta:
        verbose_name_plural = 'Трек-номера'

    id = models.CharField(
        max_length=50,
        primary_key=True,
        verbose_name='Трек'
    )
    # status_choices = [
    #     ('new', '📝 Добавлен'),
    #     ('eha', '🚚 В пути'),
    #     ('tut', '🗿 Ожидает'),
    #     ('vse', '🤝 Выдан')
    # ]
    # status = models.CharField(
    #     max_length=3,
    #     choices=status_choices,
    #     default='new',
    #     verbose_name='Статус'
    # )
    status = models.ForeignKey(Status,
                               to_field='code',
                               default='new',
                               on_delete=models.SET_DEFAULT,
                               )

    status_change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class UserPackages(models.Model):
    class Meta:
        verbose_name_plural = 'Трек-номера пользователей'

    user_id = models.ForeignKey(User,
                                default=None,
                                on_delete=models.CASCADE
                                )
    package_id = models.ForeignKey(Packages,
                                   default=None,
                                   on_delete=models.CASCADE
                                   )
    desc = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user_id) + ' : ' + str(self.package_id)
