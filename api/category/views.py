from rest_framework import viewsets, permissions
from .serializers import CategorySerializer
from .models import Category


class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
