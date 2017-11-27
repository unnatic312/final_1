from django.db import models


# Create your models here.Databae tables

class users (models.Model):
    userId=models.CharField(max_length=50,default='000000000000')
    state=models.BooleanField(default=False)
    current=models.FloatField(default=00.00)
    voltage=models.FloatField(default=00.00)
    power = models.FloatField(default=00.00)
    unit = models.FloatField(default=00.00)
    cmd = models.IntegerField(default=00)
    act = models.IntegerField(default=00)

    def __str__(self):
        return self.userId



class msg(models.Model):
    topic = models.CharField(max_length=50)
    payload = models.CharField(max_length=200)
    qos = models.SmallIntegerField()
    host = models.CharField(max_length=20)
    port = models.IntegerField()
    user = models.CharField(max_length=10)

    def __str__(self):
        return (self.user)


