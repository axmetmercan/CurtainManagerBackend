from django.shortcuts import render
from rest_framework import viewsets, mixins
from ..models import Brand, Curtain, Color,Category
from ..serializers import BrandSerializer, CurtainSerializer
from company.models import Dealers, Company
from itertools import chain
from rest_framework import permissions as per
from django.db.models import F
from ..pagination import DefaultPagination

# ORM Queries will be optimized when it gets larger.
# !Lots of sql queries that slows db.
class CurtainListViewSet(viewsets.ModelViewSet):

    serializer_class = CurtainSerializer
    permission_classes = [per.IsAuthenticated]
    pagination_class = DefaultPagination


    def get_queryset(self):


        # curtains = Curtain.objects.select_related('brand_company').filter(brand_company__owner = self.request.user.company)


        # company = Company.objects.get(id = self.request.user.company.id)
        # whole_salers = company.whole_salers.all()

        # whole_salers = Dealers.objects.select_related('whole_saler').filter(dealer=self.request.user.company)

        # curtains = Curtain.objects.select_related()
        # for i in whole_salers:
        #     print(i.whole_saler)


        curtains_dealers = Curtain.objects.filter(
            brand_company__in=Dealers.objects.values('whole_saler').filter(dealer=self.request.user.company))
        
        return curtains_dealers
    
    def perform_create(self,serializer):

        color = self.request.data.get('color')


        brand = Brand.objects.get(owner = self.request.user.company)
        color = Color.objects.get(color=color)
        category = Category.objects.get(name=self.request.data.get('category'))
        
        instance = serializer.save(brand=brand,
                                   brand_company=self.request.user.company, 
                                   color=color,
                                   category = category)
    