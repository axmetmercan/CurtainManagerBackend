from django.db import models
from company.models import Company
# Create your models here.


class Customer(models.Model):
    customer_of = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Müşterisi Olduğu Şirket' ,related_name='companies', blank=False, null=False)
    name = models.CharField(max_length=100, blank=False ,null=False, verbose_name='Müşteri Adı')
    surname = models.CharField(max_length=100, blank=False ,null=False, verbose_name='Müşteri Soyadı')
    phone = models.BigIntegerField(verbose_name='Telefon Numarası')
    email = models.EmailField(max_length=100, blank=False, null=False, verbose_name='Email')
    address = models.CharField(max_length=100, blank=False,null=False, verbose_name='Açık Adres')
    tc_no = models.BigIntegerField(verbose_name='Tc Kimlik Numarası')


    def __str__(self) -> str:
        return str(self.name + " " + self.surname)

    class Meta:
        verbose_name = 'Müşteri'
        verbose_name_plural = 'Müşteriler'