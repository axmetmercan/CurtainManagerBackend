from django.db import models
from customer.models import Customer
from company.models import Company

class MeasurementGroup(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False, verbose_name='Ölçü Grubu Adı')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name= "measurement_groups", verbose_name='Müşteri Adı', blank=False, null=False)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='Şirket Adı', blank=False, null=False)


    def __str__(self) -> str:
        return str(self.name)


    class Meta:
        verbose_name='Ölçü Grubu'
        verbose_name_plural='Ölçü Grupları'