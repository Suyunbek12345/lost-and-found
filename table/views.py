
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework import filters, status
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Storage
from .serializers import StorageListSerializer, StorageCreateSerializer
from django_filters import rest_framework as rest_filter

from .permissions import IsOwner




class StorageViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageListSerializer
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
            return StorageListSerializer
        elif self.action == 'create':
            return StorageCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()


# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.filter(in_stock=True)
# product.object.filter(in_stock=True)


class FindViewSet(ListAPIView):
    queryset = Storage.objects.filter(storage='find')
    serializer_class = StorageListSerializer


class LostViewSet(ListAPIView):
    queryset = Storage.objects.filter(storage='lost')
    serializer_class = StorageListSerializer
