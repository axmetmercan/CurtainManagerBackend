from django.db import models
from company.models import Company

class Dealers(models.Model):
    dealer = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="Bayi ID", related_name="dealers")
    whole_saler = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name="Toptancı ID", related_name="whole_salers", default=1)


    def __str__(self):

        return str(self.dealer)

    class Meta:
        verbose_name='Bayi'
        verbose_name_plural='Bayiler'

        
