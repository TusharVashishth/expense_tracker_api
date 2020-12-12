from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'user', 'category', 'created_at')
    list_display_links = ('title', 'amount')


admin.site.register(Expense, ExpenseAdmin)
