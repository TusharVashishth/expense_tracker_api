from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework import permissions


class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]
