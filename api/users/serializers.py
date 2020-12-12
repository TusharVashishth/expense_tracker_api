from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
