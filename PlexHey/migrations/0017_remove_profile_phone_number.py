# Generated by Django 2.1.7 on 2019-06-28 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlexHey', '0016_car_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Phone_Number',
        ),
    ]