# Generated by Django 2.2.4 on 2019-08-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('houses', '0004_auto_20190816_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='bike_score',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='house',
            name='transit_score',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='house',
            name='walk_score',
            field=models.IntegerField(default=-1),
        ),
    ]