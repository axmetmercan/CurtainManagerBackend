from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from ..models import Brand
from ..serializers import BrandSerializer
from company.models import Dealers
from itertools import chain
from ..pagination import DefaultPagination
# Create your views here.


class BrandsListView(viewsets.GenericViewSet,
                    mixins.ListModelMixin):
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
    
    
    def get_queryset(self):

        current_company = self.request.user.company
        # #Select the whole salers to find which brands belongs them        
        whole_salers = Dealers.objects.filter(dealer= current_company)
        quer = []
        for whole_saler in whole_salers:

            brands_of_whole_saler = Brand.objects.filter(owner=whole_saler.whole_saler)
            quer = list(chain(brands_of_whole_saler))
        
        
        own_brands = Brand.objects.filter(owner = current_company)
        

        return list(chain(own_brands ,quer))
