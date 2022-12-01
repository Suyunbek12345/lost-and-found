
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from slugify import slugify


User = get_user_model()

CHOICES = (
        ('lost', 'Потерял'),
        ('find', 'Нашел')
    )

class Advert(models.Model):

    type = models.CharField(max_length=50, choices=CHOICES)

    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User,
        on_delete=models.CASCADE,
        related_name='publication'
    )
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

    slug = models.SlugField(max_length=100, primary_key=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )
    title = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    number = models.CharField(max_length=13)
    image = models.ImageField(upload_to='images', null=True, blank=True)




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

class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.book} -> {self.created_at}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


