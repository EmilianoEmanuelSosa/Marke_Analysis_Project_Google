# Generated by Django 4.2.4 on 2023-09-05 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api_project', '0010_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]