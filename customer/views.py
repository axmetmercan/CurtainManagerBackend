from rest_framework import viewsets, permissions
from .models import Customer
from .serializers import CustomerSerializer
from .pagination import DefaultPagination

# Create your views here.


class CustomerCRUDViewset(viewsets.ModelViewSet):


    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination


    def get_queryset(self):

        return Customer.objects.filter(customer_of = self.request.user.company)
    

    def perform_create(self, serializer):
        
        instance = serializer.save(

            customer_of = self.request.user.company,
        )


        
        return super().perform_create(serializer)