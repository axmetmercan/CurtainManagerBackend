from django.db import models

# Create your models here.


class Color(models.Model):
    color = models.CharField(max_length=100, verbose_name='Renk', blank=False, null=False)


    def __str__(self):
        return str(self.color)

    class Meta:
        verbose_name = "Renk"
        verbose_name_plural = "Renkler"
  
  