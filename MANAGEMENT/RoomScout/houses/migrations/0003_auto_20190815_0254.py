# Generated by Django 2.2.4 on 2019-08-15 02:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('houses', '0002_house_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='lat',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='house',
            name='lon',
            field=models.TextField(default=''),
        ),
    ]
