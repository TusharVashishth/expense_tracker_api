from django.db import models
from django.core import validators
from api.users.models import CustomUser
from api.category.models import Category


class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='expense_user')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True , related_name="expense_category")
    title = models.CharField(max_length=300, null=True, validators=[validators.MinLengthValidator(3)])
    amount = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
