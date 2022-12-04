from rest_framework import serializers

from .models import Advert, Comment, Favorites


class AdvertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ('user', 'title', 'category', 'date')



class AdvertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = 'image',


class AdvertCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        model = Advert
        fields = '__all__'

    def create(self, validated_data):
        post = Advert.objects.create(**validated_data)
        return post


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




   # def validate(self, attrs):
    #     a = self._context['request']
    #     if "+996" not in a.phone:
    #         raise serializers.ValidationError(
    #             'Your number is not from Kyrgyzstan! Salamalekym! Davay brat menyi! Change your number'
    #         )
    #     if len(a.slug) < 8:
    #         raise serializers.ValidationError(
    #             'As`salam Aleikym. Please, po bratske write minimum 8 symbols.'
    #         )
    #     return attrs
