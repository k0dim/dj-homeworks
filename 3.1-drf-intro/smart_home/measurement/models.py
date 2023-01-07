from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=64, verbose_name='Наименование датчика')
    description = models.CharField(max_length=128, verbose_name='Описание')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement', verbose_name='ID дтчика')
    temperature = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Температра')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return f"{self.sensor_id} - {self.temperature}"
