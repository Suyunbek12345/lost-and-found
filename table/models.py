
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from slugify import slugify


User = get_user_model()

CHOICES = (
        ('lost', 'Потерял'),
        ('find', 'Нашел')
    )

class Storage(models.Model):

    type = models.CharField(max_length=50, choices=CHOICES)

    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User,
        on_delete=models.CASCADE,
        related_name='publication'
    )

    slug = models.SlugField(max_length=170, primary_key=True)
    title = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    number = models.CharField(max_length=13)
    image = models.ImageField(upload_to='images', null=True, blank=True)


    CATEGORY_CHOICES = (
        ('documents', 'Документ'),
        ('keys', 'Ключи'),
        ('electronik', 'электроника'),
        ('animals', 'Животные'),
        ('jewelry', 'Драгоценности'),
        ('bags', 'Сумки'),
        ('phones', 'телефоны'),
        ('other', 'Другое'),

    )

    ADDRESS_CHOICES = (
        ('Balykchy', 'Балыкчы'),
        ('Bishkek', 'Бишкек'),
        ('Kant', 'Кант'),
        ('Karakol', 'Каракол'),
        ('Naryn', 'Нарын'),
        ('Osh', 'Ош'),
        ('Talas', 'Талас'),
        ('Tokmok', 'Токмок'),

    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    address = models.CharField(max_length=100, choices=ADDRESS_CHOICES)
    whatsapp = models.CharField(max_length=13, null=True, blank=True)
    date = models.DateField(verbose_name='Дата находки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


