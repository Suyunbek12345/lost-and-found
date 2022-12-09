from django.db.models import Q
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from . import serializers
from .models import Advert, Comment
from .permissions import IsAuthor
from rest_framework.response import Response
from rest_framework import generics
from .models import Favorites
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AdvertListSerializer


class AdvertViewSet(ModelViewSet):
    queryset = Advert.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'user', 'author_name')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AdvertListSerializer
        return serializers.AdvertDetailSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        elif self.action in ('create', 'favorite_action', 'remove_from_favorites'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save()

    @action(['POST'], detail=True)
    def comments(self, request, pk):
        advert = self.get_object()
        user = request.user
        Comment.objects.create(owner=user, advert=advert)
        return Response('You put comment!', status=201)

    @action(['GET'], detail=True)
    def get_comments(self, request, pk):
        advert = self.get_object()
        comments = Advert.comments.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)

    @action(['POST'], detail=True)
    def favorite_action(self, request, pk):
        advert = self.get_object()
        user = request.user
        if user.favorites.filter(advert=advert).exists():
            user.favorites.filter(advert=advert).delete()
            return Response('Deleted From Favorites!', status=204)
        Favorites.objects.create(user=user, advert=advert)
        return Response('Added to Favorites!', status=201)

    @action(['DELETE'], detail=True)
    def remove_from_favorites(self, request, pk):
        advert = self.get_object()
        user = request.user
        if not user.favorites.filter(advert=advert).exists():
            return Response('This Advert is not in Favorites!', status=400)
        user.favorites.filter(advert=advert).delete()
        return Response('Your Favorite is Deleted!', status=204)

    @action(['GET'], detail=True)
    def get_favorites(self, request, pk):
        advert = self.get_object()
        favorites = advert.favorites.all()
        serializer = serializers.FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)


class FindViewSet(ListAPIView):
    queryset = Advert.objects.filter(type='find')
    serializer_class = AdvertListSerializer


class LostViewSet(ListAPIView):
    queryset = Advert.objects.filter(type='lost')
    serializer_class = AdvertListSerializer





# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class PostView(generics.ListCreateAPIView):
#     queryset = Advert.objects.all()
#     serializer_class = AdvertListSerializer
#
#
# class AdvertDetailView(generics.RetrieveAPIView):
#     queryset = Advert.objects.all()
#     serializer_class = AdvertListSerializer
#
#
# class AdvertUpdateView(generics.UpdateAPIView):
#     queryset = Advert.objects.all()
#     serializer_class = AdvertListSerializer
#
#
# class AdvertDeleteApiView(generics.DestroyAPIView):
#     queryset = Advert.objects.all()
#     serializer_class = AdvertListSerializer












