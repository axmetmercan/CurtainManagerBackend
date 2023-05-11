from django.db import models
from product.models import Curtain
from company.models import Company


class DealerOrder(models.Model):
    status = models.CharField(max_length=100, blank=False, null=False, verbose_name='Sipariş Durumu')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Oluşturma Tarihi')
    unit_price= models.FloatField(verbose_name='Birim Fiyatı')
    unit = models.FloatField(verbose_name='Birim Miktarı')
    payment = models.FloatField(verbose_name='Sipariş İçin Yapılan Ödeme', default=0)
    product = models.ForeignKey(Curtain, on_delete=models.DO_NOTHING, related_name='dealer_products', verbose_name='Ürün', blank=False, null=False)
    dealer_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, related_name='dealer_companies', verbose_name='Bayi', blank=False, null=False)
    product_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,  related_name='product_companies',verbose_name='Üretici', blank=False, null=False)


    class Meta:
        
        verbose_name='Bayi Üretici Sipariş'
        verbose_name_plural='Bayi Üretici Siparişleri'