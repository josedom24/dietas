from django.db import models

# Create your models here.

class Alimentos(models.Model):
    nombre = models.CharField(default="",max_length=100)
    proteinas = models.FloatField(verbose_name="Proteinas (gr)")
    grasas = models.FloatField(verbose_name="Grasas (gr)")
    carbohidratos = models.FloatField(verbose_name="Carbohidratos (gr)")
    kilocalorias = models.FloatField(verbose_name="Kilocalorias (kcal)")
    porcion_comestible = models.FloatField(verbose_name="Porción comestible (gr)")

    class Meta:
        verbose_name="Alimento"
        verbose_name_plural="Alimentos"
