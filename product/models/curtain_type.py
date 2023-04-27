from django.db import models


class CurtainType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Perde Tipi Adı')


    class Meta:
        verbose_name = 'Perde Model Tipi'
        verbose_name_plural ='Perde Model Tipleri'