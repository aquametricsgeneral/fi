from django.db import models

class AlertSetting(models.Model):
    MH0001_TEMP = 'mh0001_temp'
    MH0001_HUMIDITY = 'mh0001_humidity'
    MH0002_TEMP = 'mh0002_temp'
    MH0002_HUMIDITY = 'mh0002_humidity'
    MH0003_TEMP = 'mh0003_temp'
    MH0003_HUMIDITY = 'mh0003_humidity'

    SENSOR_CHOICES = ((MH0001_TEMP, 'MH0001_TEMP'), (MH0001_HUMIDITY, 'MH0001_HUMIDITY'),
                    (MH0002_TEMP, 'MH0002_TEMP'), (MH0002_HUMIDITY, 'MH0002_HUMIDITY'),
                    (MH0003_TEMP, 'MH0003_TEMP'), (MH0003_HUMIDITY, 'MH0003_HUMIDITY'))

    sensor = models.CharField(max_length=30, choices=SENSOR_CHOICES, default=MH0001_TEMP, primary_key=True)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    slider = models.CharField(max_length=100, default='slider')
    label = models.CharField(max_length=30, default='label')
    order = models.IntegerField(default=1)

class MH0001_TEMP(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class MH0001_HUMIDITY(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class MH0002_TEMP(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class MH0002_HUMIDITY(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class MH0003_TEMP(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)

class MH0003_HUMIDITY(models.Model):
    datetime = models.DateTimeField()
    value = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    alert = models.BooleanField(default=True)
    lowerlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    upperlimit = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    withinlimit = models.BooleanField(default=True)
