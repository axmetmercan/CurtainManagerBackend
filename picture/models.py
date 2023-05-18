from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='Başlık')
    pic_url = models.ImageField(upload_to="%Y/%m/%d/", blank=True)
    uploaded_by = models.ForeignKey('company.Company', null=True, blank=True, default=1, on_delete=models.CASCADE, related_name='uploaded_by', verbose_name='Yükleyici',)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = "Resimler"

    