from django.shortcuts import render
from rest_framework import viewsets, mixins,permissions
from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.


class CustomerCRUDViewset(viewsets.ModelViewSet):


    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return Customer.objects.filter(customer_of = self.request.user.company)