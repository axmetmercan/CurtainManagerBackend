from django.db import models

# Create your models here.


class Picture(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    pic_url = models.ImageField(upload_to="%Y/%m/%d/", blank=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = "Resimler"

    