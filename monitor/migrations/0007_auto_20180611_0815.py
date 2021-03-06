# Generated by Django 2.0.4 on 2018-06-11 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20180611_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envhumidity',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='envhumidity',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='envhumidity',
            name='less',
        ),
        migrations.RemoveField(
            model_name='envhumidity',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='envtemp',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='envtemp',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='envtemp',
            name='less',
        ),
        migrations.RemoveField(
            model_name='envtemp',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='isfilling',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='isfilling',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='isfilling',
            name='less',
        ),
        migrations.RemoveField(
            model_name='isfilling',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='waterflowfishtank',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='waterflowfishtank',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='waterflowfishtank',
            name='less',
        ),
        migrations.RemoveField(
            model_name='waterflowfishtank',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='waterflowhorizgrow',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='waterflowhorizgrow',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='waterflowhorizgrow',
            name='less',
        ),
        migrations.RemoveField(
            model_name='waterflowhorizgrow',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='waterflowmain',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='waterflowmain',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='waterflowmain',
            name='less',
        ),
        migrations.RemoveField(
            model_name='waterflowmain',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='waterflowvertgrow',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='waterflowvertgrow',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='waterflowvertgrow',
            name='less',
        ),
        migrations.RemoveField(
            model_name='waterflowvertgrow',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='waterlevelfull',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='waterlevelfull',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='waterlevelfull',
            name='less',
        ),
        migrations.RemoveField(
            model_name='waterlevelfull',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='waterlevellow',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='waterlevellow',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='waterlevellow',
            name='less',
        ),
        migrations.RemoveField(
            model_name='waterlevellow',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='waterph',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='waterph',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='waterph',
            name='less',
        ),
        migrations.RemoveField(
            model_name='waterph',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='watertempfishtank',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='watertempfishtank',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='watertempfishtank',
            name='less',
        ),
        migrations.RemoveField(
            model_name='watertempfishtank',
            name='threshold',
        ),
        migrations.RemoveField(
            model_name='watertempsumptank',
            name='criteria',
        ),
        migrations.RemoveField(
            model_name='watertempsumptank',
            name='greater',
        ),
        migrations.RemoveField(
            model_name='watertempsumptank',
            name='less',
        ),
        migrations.RemoveField(
            model_name='watertempsumptank',
            name='threshold',
        ),
    ]
