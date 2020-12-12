from rest_framework import routers
from django.urls import include, path
from .views import CustomUserViewset

router = routers.DefaultRouter()

router.register(r'', CustomUserViewset)

urlpatterns = [
    path('', include(router.urls))
]
