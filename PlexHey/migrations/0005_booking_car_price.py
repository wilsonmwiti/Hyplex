# Generated by Django 2.1.7 on 2019-06-04 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlexHey', '0004_auto_20190603_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='car_price',
            field=models.PositiveIntegerField(default=True, null=True),
        ),
    ]
