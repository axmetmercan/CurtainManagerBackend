from django.db import models
from company.models import Company
# Create your models here.


class Brand(models.Model):

    title = models.CharField(max_length=100, null=False,
                             verbose_name='İsim', blank=False, default="CutainManager")
    owner = models.ForeignKey(Company, on_delete=models.CASCADE,
                              verbose_name='Üretici Şirket', null=False, blank=False, default=0)

    class Meta:
        verbose_name = 'Marka'
        verbose_name_plural = 'Markalar'
