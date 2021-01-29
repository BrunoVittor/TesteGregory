from django.db import models


class Carros(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=100)
    placa = models.CharField(max_length=50)

    def __str__(self):
        return self.marca
