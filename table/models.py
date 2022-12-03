from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_admin_geomap import GeoItem

from category.models import Category


User = get_user_model()


class Advert(models.Model):

    type = models.CharField(max_length=50)

    user = models.ForeignKey(
        verbose_name='Автор поста',
        to=User,
        on_delete=models.CASCADE,
        related_name='publication'
    )

    title = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=9)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=13, null=True, blank=True)
    date = models.DateField(verbose_name='Дата находки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('created_at',)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.advert} -> {self.created_at}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'



class Location(models.Model, GeoItem):

    @property
    def geomap_longitude(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_latitude(self):
        return self.geomap_popup_view

