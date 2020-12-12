from rest_framework import routers
from django.urls import include, path
from .views import CategoryViewset

router = routers.DefaultRouter()

router.register(r'', CategoryViewset)

urlpatterns = [
    path('', include(router.urls))
]
