from rest_framework import serializers
from .models import Category
# from api.expense.serializers import


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3)
    image = serializers.ImageField(required=True)

    class Meta:
        model = Category
        fields = '__all__'
