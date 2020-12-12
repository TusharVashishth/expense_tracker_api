from rest_framework import routers
from django.urls import path, include
from .views import ExpenseViewSet

router = routers.DefaultRouter()
router.register(r'', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls))
]
