from django.contrib import admin
from table.models import Advert, Comment, Location
from django_admin_geomap import ModelAdmin
# Register your models here.


# class Admin(ModelAdmin):
#     geomap_field_longitude = "id_lon"
#     geomap_field_latitude = "id_lat"
#

admin.site.register(Advert)
admin.site.register(Comment)
admin.site.register(Location)
