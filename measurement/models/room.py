from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, blank=False,null=False, verbose_name='Oda Adı')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name='Oda'
        verbose_name_plural='Odalar'