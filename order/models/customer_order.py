from  django.db import models
from measurement.models import Measurement, MeasurementGroup
# from product.models import Curtain
from customer.models import Customer
from company.models import Company
from product.models import Unit



ORDER_STATUS = (

    ("active", "Aktif"),
    ("preparing", "Hazırlanıyor"),
    ("on_delivery", "Teslimatta"),
    ('delivered', "Teslim Edildi"),
    ('waiting_payment', "Ödeme Bekliyor"),
    ('completed', 'Tamamlandı')
)

class CustomerOrder(models.Model):
    status = models.CharField( choices=ORDER_STATUS, max_length=100, blank=False, null=False, verbose_name='Sipariş Durumu')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Oluşturma Tarihi')
    measurement = models.ForeignKey(Measurement, on_delete=models.DO_NOTHING, verbose_name='Ölçüler', related_name='measurements' ,blank=False, null=False)
    measurement_group = models.ForeignKey(MeasurementGroup, on_delete=models.DO_NOTHING, verbose_name='Ölçü Grubu', related_name='measurement_groups', null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='customers', verbose_name='Müşteri', default=1, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=4, null=False, blank=False, verbose_name='Müşterinin Şirketi',related_name='customers')
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, verbose_name='Birim', null=False, blank=False, default=1)
    class Meta:

        verbose_name='Müşteri Siparişi'
        verbose_name_plural='Müşteri Siparişleri'


    def __str__(self):
        return str(self.measurement_group)