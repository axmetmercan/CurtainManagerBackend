from django.db import models
from picture.models import Picture

class Company(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False, verbose_name="Company Name")
    owner_name = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Owner Name")
    owner_surname = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Owner Surname")
    tc_no = models.BigIntegerField(
        null=False, blank=False, verbose_name="Personal Tax Number")
    phone_number = models.BigIntegerField(
         blank=False, null=False, verbose_name="Company Phone Number")
    email = models.EmailField(
        max_length=100, blank=False, null=False, verbose_name="Company Email")
    tax_no = models.BigIntegerField(
        null=False, blank=False, verbose_name="Tax Number")
    tax_municipilaty = models.CharField(max_length=100, blank=False,
                                        null=False, verbose_name="Municiplaty Name")
    address = models.CharField(max_length=255, blank=False, null=False)
    tax_document_pic = models.ForeignKey(Picture, related_name="pictures", on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):

            return str(self.name)

    class Meta:
        verbose_name = "Şirket"
        verbose_name_plural = "Şirketler"