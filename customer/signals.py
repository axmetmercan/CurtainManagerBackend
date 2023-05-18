from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer
from measurement.models import MeasurementGroup


@receiver(post_save, sender=Customer)
def create_new_measurement(sender, instance, created, **kwargs):
    if created:
        #Creates user for the company
        MeasurementGroup.objects.create(
                    
                        name = str(instance.name + " Yeni Ölçü"),
                        customer = instance,
                        company = instance.customer_of,
                                 )
        

    
