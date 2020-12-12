from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_joined', 'is_staff', 'is_active')
    list_display_links = ('email', 'name')


admin.site.register(CustomUser, CustomUserAdmin)
