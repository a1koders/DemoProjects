# Generated by Django 2.2.4 on 2019-10-12 22:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bills', '0013_auto_20190908_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billset',
            options={'ordering': ['year', 'month']},
        ),
    ]