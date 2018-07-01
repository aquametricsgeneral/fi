from django.db import models

class MH0001(models.Model):
    datetime = models.DateTimeField()
    temp = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class MH0002(models.Model):
    datetime = models.DateTimeField()
    temp = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class MH0003(models.Model):
    datetime = models.DateTimeField()
    temp = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    humidity = models.DecimalField(max_digits=5, decimal_places=2, default=0)

class health(models.Model):
    datetime = models.DateTimeField()
    command = models.CharField(max_length=10)
