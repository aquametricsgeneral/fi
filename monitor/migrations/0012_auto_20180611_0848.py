# Generated by Django 2.0.4 on 2018-06-11 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_auto_20180611_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envhumidity',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
