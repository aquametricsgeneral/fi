# Generated by Django 2.0.4 on 2018-06-11 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0016_auto_20180611_1108'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WaterLevelFull',
        ),
        migrations.DeleteModel(
            name='WaterLevelLow',
        ),
    ]