# Generated by Django 5.1.5 on 2025-01-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm_app', '0002_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]