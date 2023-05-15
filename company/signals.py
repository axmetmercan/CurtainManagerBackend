from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company,Dealers
from user.models import User, UserType
from product.models import Brand
"""
Creates an admin privileges user with the 
name = Company owner name
email = Company email
password = Company owner tc no
"""

@receiver(post_save, sender=Company)
def create_company_admin(sender, instance, created, **kwargs):
    if created:

        #Creates user for the company
        User.objects.create_user(
                        
                        name = instance.owner_name,
                        password=instance.owner_surname,
                        surname=instance.owner_surname,
                        phone_number=instance.phone_number,
                        email = instance.email,
                        tc_number = instance.tc_no,
                        salary = 0,
                        type = UserType.objects.get(title='admin'),
                        company = instance,
                                 )
        

        #Creates brands for the itself of that company
        Brand.objects.create(title = instance.name, owner = instance)
        #Creates Dealership for itself of that company
        Dealers.objects.create(dealer= instance, whole_saler=instance)
    
    
    
    
    # if created:
    #     Employee.objects.create_user(
    #         name = instance.owner_name,
    #         surname=instance.owner_surname,
    #         email=instance.email,
    #         password=str(instance.tc_no),
    #         tc_number = instance.tc_no,
    #         phone_number=instance.phone_number,
    #         type=EmployeeType.objects.get(title = "admin"),
    #         company = instance
    #     )
