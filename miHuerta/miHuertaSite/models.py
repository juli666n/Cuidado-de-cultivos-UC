from django.db import models


class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    temperature = models.FloatField()
    moisture = models.FloatField()
    lux = models.FloatField()
    isSelected = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.name, self.description)


class Sensor(models.Model):

    temperatureSensor = models.FloatField()
    moistureSensor = models.FloatField()
    luxSensor = models.FloatField()


class Actuator(models.Model):

    temperatureActuator = models.BooleanField()
    moistureActuator = models.BooleanField()
    luxActuator = models.BooleanField()
