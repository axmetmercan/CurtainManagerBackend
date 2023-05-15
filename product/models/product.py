from django.db import models
from .brands import Brand
from company.models import Company, Dealers
from .color import Color
from picture.models import Picture
from .category import Category


# Create your models here.


class Curtain(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, verbose_name='Marka', related_name="brands", blank=False, null=False)
    brand_company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name='Üretici Şirket', related_name="brand_companies", blank=False, null=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Kategori', related_name='categories', blank=False, null=False)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, verbose_name='Renk', related_name='colors', blank=False, null=False)
    code = models.CharField(max_length=200, verbose_name="Barkod")
    variant = models.CharField(
        max_length=200, verbose_name='Varyant', blank=True, null=True)
    weight = models.IntegerField(null=True, blank=True, verbose_name='Gramaj')
    height = models.IntegerField(
        null=True, blank=True, verbose_name='Yükseklik')
    w_price = models.FloatField(
        null=False, blank=False, verbose_name="Toptan Fiyatı")
    s_price = models.FloatField(
        null=False, blank=False, verbose_name="Satış Fiyatı")
    # unit_type =
    img1 = models.ForeignKey(
        Picture, on_delete=models.DO_NOTHING, verbose_name='Resim1', related_name='img1s', null=True, blank=True)
    img2 = models.ForeignKey(
        Picture, on_delete=models.DO_NOTHING, verbose_name='Resim1', related_name='img2s', null=True, blank=True)

    img3 = models.ForeignKey(
        Picture, on_delete=models.DO_NOTHING, verbose_name='Resim1', related_name='img3s',  null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)


    def __str__(self):
        return str(self.code)


    class Meta:
        verbose_name='Ürün'
        verbose_name_plural='Ürünler'