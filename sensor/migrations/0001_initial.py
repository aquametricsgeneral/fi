# Generated by Django 2.0.4 on 2018-06-26 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MH0001',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MH0002',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MH0003',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('temp', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
    ]
