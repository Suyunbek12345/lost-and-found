from rest_framework import serializers

from category.models import Category
from .models import Advert, Comment, Favorites


class AdvertListSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S')
    class Meta:
        model = Advert
        fields = ('id', 'user', 'title', 'description', 'name', 'last_name', 'category', 'address', 'whatsapp')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = instance.images.all()


class AdvertDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Advert
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'advert', 'owner')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('advert',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['advert'] = AdvertListSerializer(instance.post).data
        return repr

