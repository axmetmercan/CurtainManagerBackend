from django.db import models

# Create your models here.


class Color(models.Model):
    color = models.CharField(max_length=100, verbose_name='Renk', blank=False, null=False)

    class Meta:
        verbose_name = "Renk"
        verbose_name_plural = "Renkler"
  
  