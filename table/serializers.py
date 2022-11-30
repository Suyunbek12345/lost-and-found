from rest_framework import serializers

from .models import Storage


class StorageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('storage', 'user', 'title', 'image', 'status', 'category', 'address', 'date')


# class StorageSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')

#     class Meta:
#         model = Storage
#         fields = ('storage','user', 'title', 'image', 'status', 'text', 'category', 'address', 'date' )


class StorageImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = 'image',


class StorageCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        model = Storage
        fields = '__all__'


    def create(self, validated_data):
        post = Storage.objects.create(**validated_data)
        return post

