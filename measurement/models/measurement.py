from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from product.models import Curtain
from .room import Room
from .measurement_group import MeasurementGroup

class Measurement(models.Model):
    measurement_group = models.ForeignKey( MeasurementGroup, on_delete=models.DO_NOTHING ,blank=False, null=False, verbose_name='Ölçü Grup Idsi')
    room_name = models.ForeignKey(Room, on_delete=models.DO_NOTHING, verbose_name='Oda Adı')
    width = models.IntegerField(verbose_name='Genişlik',blank=False, null=False, validators=[MaxValueValidator(600), MinValueValidator(30)])
    height =models.IntegerField(verbose_name='Yükseklik', blank=False, null=False, validators=[MaxValueValidator(600), MinValueValidator(50)])
    measurement_note = models.CharField(max_length=(255), verbose_name='Ölçü Notu', blank=True, null=True)
    unit_price = models.FloatField(verbose_name='Birim Fiyatı', null=False, blank=False, validators=[MinValueValidator(0)])
    room_pic = models.ImageField(upload_to='measurement/windows/%Y/%m/%d', verbose_name='Pencere Resmi')
    product = models.ForeignKey(Curtain, on_delete=models.DO_NOTHING, related_name='products', verbose_name='Ürün')

    class Meta:
        verbose_name='Ölçü'
        verbose_name_plural='Ölçüler'