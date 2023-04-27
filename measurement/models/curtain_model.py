from django.db import models


class CurtainModel(models.Model):
    name = models.CharField(max_length=100, blank=False,null=False, verbose_name='Perde Model Adı')

    class Meta:
        verbose_name='Perde Modeli'
        verbose_name_plural='Perde Modelleri'