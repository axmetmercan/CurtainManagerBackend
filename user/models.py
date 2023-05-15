from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from company.models import  Company
# Create your models here.


EMPLOYEE_TITLE = (

    ("admin", "Admin"),
    ("salesman", "Salesman"),
    ("worker", "Worker"),
)



class UserType(models.Model):
    title = models.CharField(choices=EMPLOYEE_TITLE,max_length=200, blank=True, null=True, default="worker")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Çalışan Tipi'
        verbose_name_plural = 'Çalışan Tipleri'




class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, 
                    email, 
                    password, 
                    phone_number, 
                    name,
                    surname,
                    **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_deleted', False)
        user = self.model(name = name,
                          email=email,
                          surname = surname,
                          phone_number = phone_number,
                         **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    
    name = models.CharField(max_length=65, blank=False, null=False ,verbose_name='Employee Name')
    surname = models.CharField(max_length=100, blank=False, null=False, verbose_name='Employee Surname')
    phone_number = models.BigIntegerField(verbose_name='Employee Phone Number',  blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False ,verbose_name='Employee Email', unique=True)
    tc_number = models.BigIntegerField(blank=False, null=False ,verbose_name='Employee National ID')
    salary = models.IntegerField(verbose_name='Salary', default=None, null=True, blank=True)
    type = models.ForeignKey(UserType , null=True, blank=True, on_delete=models.DO_NOTHING)
    company=models.ForeignKey(Company,verbose_name='Company', on_delete=models.CASCADE, null=True, blank=True )

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    is_active=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)

    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name', 'surname' ,'phone_number', 'tc_number']

    objects = CustomUserManager()

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_tc_number(self):
        return self.tc_number

    # def __str__(self):
    #     return self.name
        

    class Meta:
        verbose_name = 'Çalışan'
        verbose_name_plural = 'Çalışanlar'


