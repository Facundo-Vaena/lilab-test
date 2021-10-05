from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

bueno = 'bueno'
regular = 'regular'
malo = 'malo'
options = [bueno, regular, malo]

class Solicitante(models.Model) :
    nombre = models.CharField(max_length=50)
    deuda_total_SBS = models.CharField(max_length=50)
    puntaje_deudor = models.CharField(max_length=50)
    puntaje_IA = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    monto_credito = models.IntegerField()

    #   choices=['bueno', 'regular', 'malo']