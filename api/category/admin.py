from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',  'image_tag')
    list_display_links = ('name',)
    readonly_fields = ('image_tag',)


admin.site.register(Category, CategoryAdmin)
