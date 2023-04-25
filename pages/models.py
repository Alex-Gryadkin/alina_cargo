from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категории'

    position = models.IntegerField(
        verbose_name='Порядок',
        default=1
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=100,
    )

    @classmethod
    def get_default_cat(cls):
        cat, created = cls.objects.get_or_create(
            title='root',
            defaults=dict(position=0),
        )
        return cat.pk

    def __str__(self):
        return self.title


class Page(models.Model):
    class Meta:
        verbose_name_plural = 'Страницы'
        default_related_name = 'pages'

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
    is_visible = models.BooleanField(
        verbose_name='Видимость',
        default=False
    )
    position = models.IntegerField(
        verbose_name='Порядок',
    )
    category = models.ForeignKey(
        Category,
        default=Category.get_default_cat(),
        on_delete=models.SET_DEFAULT,
    )

    def __str__(self):
        return str(self.title)

