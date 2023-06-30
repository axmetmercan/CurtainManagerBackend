from django.db import models
from product.models import Curtain, Unit
from company.models import Company


ORDER_STATUS = (

    ("active", "Aktif"),
    ("preparing", "Hazırlanıyor"),
    ("on_delivery", "Teslimatta"),
    ('delivered', "Teslim Edildi"),
    ('waiting_payment', "Ödeme Bekliyor"),
    ('completed', 'Tamamlandı')
)


class DealerOrder(models.Model):
    status = models.CharField(choices=ORDER_STATUS, max_length=100, blank=False, null=False, verbose_name='Sipariş Durumu')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Oluşturma Tarihi')
    unit_price= models.FloatField(verbose_name='Birim Fiyatı')
    unit = models.FloatField(verbose_name="Birim")
    unit_type = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, verbose_name='Birim Tipi', null=False, blank=False, default=1)
    payment = models.FloatField(verbose_name='Sipariş İçin Yapılan Ödeme', default=0)
    product = models.ForeignKey(Curtain, on_delete=models.DO_NOTHING, related_name='dealer_products', verbose_name='Ürün', blank=False, null=False)
    dealer_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, related_name='dealer_companies', verbose_name='Bayi', blank=False, null=False)
    product_company = models.ForeignKey(Company, on_delete=models.DO_NOTHING,  related_name='product_companies',verbose_name='Üretici', blank=False, null=False)
    # current_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='current_company', verbose_name='Aktif Şuanki Şirket', null=True, blank=True)

    class Meta:
        
        verbose_name='Bayi Üretici Sipariş'
        verbose_name_plural='Bayi Üretici Siparişleri'



    def __str__(self):
        return str(str(self.product_company) + " -> " +str(self.dealer_company))