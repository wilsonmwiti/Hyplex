# Generated by Django 2.1.7 on 2019-06-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlexHey', '0005_auto_20190603_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone_Number',
            field=models.CharField(default=True, max_length=13, null=True),
        ),
    ]