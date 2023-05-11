from  django.db import models
from measurement.models import Measurement, MeasurementGroup

class CustomerOrder(models.Model):
    status = models.CharField(max_length=100, blank=False, null=False, verbose_name='Sipariş Durumu')
    created_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Oluşturma Tarihi')
    measurement = models.ForeignKey(Measurement, on_delete=models.DO_NOTHING, verbose_name='Ölçüler', related_name='measurements' ,blank=False, null=False)
    measurement_group = models.ForeignKey(MeasurementGroup, on_delete=models.DO_NOTHING, verbose_name='Ölçü Grubu', related_name='measurement_groups', null=False, blank=False)


    class Meta:

        verbose_name='Müşteri Siparişi'
        verbose_name_plural='Müşteri Siparişleri'