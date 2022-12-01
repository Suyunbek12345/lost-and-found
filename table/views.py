
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework import filters, status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Advert
from .serializers import AdvertListSerializer, AdvertCreateSerializer
from django_filters import rest_framework as rest_filter

from .permissions import IsOwner


class StorageViewSet(GenericViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertListSerializer
    filter_backends = [filters.SearchFilter,
    rest_filter.DjangoFilterBackend,
    filters.OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['category']
    ordering_fields = ['created_at']


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        print(serializer)

    def get_serializer_class(self):
        if self.action == 'list':
            return AdvertListSerializer
        elif self.action == 'create':
            return AdvertCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['destroy', 'update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()


class FindViewSet(ListAPIView):
    queryset = Advert.objects.filter(type='find')
    serializer_class = AdvertListSerializer


class LostViewSet(ListAPIView):
    queryset = Advert.objects.filter(type='lost')
    serializer_class = AdvertListSerializer

