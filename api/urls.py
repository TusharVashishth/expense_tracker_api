from django.urls import path, include

urlpatterns = [
    path('expense/', include('api.expense.urls')),
    path('users/', include('api.users.urls')),
    path('category/', include('api.category.urls'))
]
