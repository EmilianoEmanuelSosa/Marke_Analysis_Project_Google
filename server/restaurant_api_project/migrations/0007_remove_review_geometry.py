# Generated by Django 4.2.4 on 2023-09-06 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api_project', '0006_remove_restaurant_geometry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='geometry',
        ),
    ]