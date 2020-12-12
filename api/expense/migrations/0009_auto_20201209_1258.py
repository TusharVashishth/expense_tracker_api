# Generated by Django 3.1.4 on 2020-12-09 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('expense', '0008_auto_20201209_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense_category', to='category.category'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expense_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
