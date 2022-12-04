from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Category
from . import serializers


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('delete', 'put'):
            return [permissions.IsAdminUser()]
        else:
            return [permissions.AllowAny()]

