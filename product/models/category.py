from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False, verbose_name='Kategori')

    class Meta:
        verbose_name = "Kategori"
        verbose_name = "Kategoriler"
