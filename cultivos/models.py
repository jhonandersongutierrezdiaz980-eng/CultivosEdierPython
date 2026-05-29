from django.db import models
from django.core.exceptions import ValidationError

def validar_cantidad(value):
    if value <= 0:
        raise ValidationError('La cantidad debe ser mayor a cero.')

class Cultivo(models.Model):
    ZONAS_CHOICES = [
        ('N', 'Zona Norte (Hortalizas)'),
        ('S', 'Zona Sur (Frutales)'),
        ('E', 'Zona Este (Legumbres)'),
        ('O', 'Zona Oeste (Aromáticas)'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre del Cultivo")
    agricultor = models.CharField(max_length=100, verbose_name="Nombre del Vecino/Agricultor")
    zona = models.CharField(max_length=1, choices=ZONAS_CHOICES, verbose_name="Zona del Huerto")
    cantidad_sembrada = models.IntegerField(validators=[validar_cantidad], verbose_name="Cantidad de Semillas/Plantas")
    fecha_siembra = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.agricultor}"
