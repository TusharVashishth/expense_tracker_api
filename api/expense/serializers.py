from rest_framework import serializers
from .models import Expense
from api.category.serializers import CategorySerializer


class ExpenseSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=False)
    # category = serializers.StringRelatedField(many=False)
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # category_img = serializers.SerializerMethodField('get_category_image')
    title = serializers.CharField(min_length=3, max_length=100)
    amount = serializers.FloatField(min_value=1)
    # category = serializers.CharField(min_length=1)

    class Meta:
        model = Expense
        fields = '__all__'

        # depth = 1
        # Fetch all data with relation

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        return rep

    # def get_category_image(self, Expense):
    #     category_img = Expense.category.image
    #     return category_img
    # def create(self, validated_data):
    #     print(validated_data)
    #     category_data = validated_data.pop('category')
    #     expense = Expense.objects.create(**validated_data)
    #     # for data in category_data:
    #     Category.objects.create(expense_category=expense, **category_data)
    #
    #     return expense
