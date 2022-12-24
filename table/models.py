from django.contrib.auth import get_user_model
from django.db import models

from category.models import Category


User = get_user_model()


class Advert(models.Model):

    CHOISES_TYPE = (
        ('find', 'найдено'),
        ('lost', 'потеряно')
    )

    type = models.CharField(max_length=200, choices=CHOISES_TYPE)

    user = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        on_delete=models.CASCADE,
        related_name='publication',
        null=True
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    phone = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Favorites(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ['owner', 'advert']


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


# class Location(models.Model, GeoItem):
#
#     @property
#     def geomap_longitude(self):
#         return "<strong>{}</strong>".format(str(self))
#
#     @property
#     def geomap_latitude(self):
#         return self.geomap_popup_view
#
