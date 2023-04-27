from django.db import models



class Unit(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Birim Tipi Adı')


    class Meta:
        verbose_name = 'Perde Birim'
        verbose_name_plural ='Perde Birimleri'