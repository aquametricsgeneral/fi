# Generated by Django 2.0.4 on 2018-06-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_auto_20180611_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterLevelHigh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('alert', models.BooleanField(default=True)),
                ('lowerlimit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('upperlimit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('withinlimit', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterLevelLow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('alert', models.BooleanField(default=True)),
                ('lowerlimit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('upperlimit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('withinlimit', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='alertsetting',
            name='sensor',
            field=models.CharField(choices=[('envtemp', 'EnvTemp'), ('envhumidity', 'EnvHumidity'), ('watertempfishtank', 'WaterTempFishTank'), ('watertempsumptank', 'WaterTempSumpTank'), ('waterph', 'WaterPH'), ('isfilling', 'IsFilling'), ('waterlevellow', 'WaterLevelLow'), ('waterlevelhigh', 'WaterLevelHigh'), ('waterflowfishtank', 'WaterFlowFishTank'), ('waterflowmain', 'WaterFlowMain'), ('waterflowvertgrow', 'WaterFlowVertGrow'), ('waterflowhorizgrow', 'WaterFlowHorizGrow')], default='envtemp', max_length=30, primary_key=True, serialize=False),
        ),
    ]
