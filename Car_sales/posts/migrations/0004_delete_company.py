# Generated by Django 5.1.2 on 2025-01-11 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]
