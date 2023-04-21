from django.db import models


class Page(models.Model):
    class Meta:
        verbose_name_plural = 'Страницы'

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=100,
    )
    slug = models.SlugField(
        verbose_name='URL',
        max_length=255,
        unique=True,
        db_index=True,
    )
    content = models.TextField(
        verbose_name='Содержание',
    )
    def __str__(self):
        return str(self.title)
