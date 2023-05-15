from django.shortcuts import render
from rest_framework import viewsets, mixins
from ..models import Brand, Curtain
from ..serializers import BrandSerializer, CurtainSerializer
from company.models import Dealers, Company
from itertools import chain
from django.db.models import F


# ORM Queries will be optimized when it gets larger.
# !Lots of sql queries that slows db.
class CurtainListViewSet(viewsets.ModelViewSet):

    serializer_class = CurtainSerializer

    def get_queryset(self):

        # curtains = Curtain.objects.select_related('brand_company').filter(brand_company__owner = self.request.user.company)

        curtains = Curtain.objects.all()

        curtains = Curtain.objects.select_related('brand')

        # company = Company.objects.get(id = self.request.user.company.id)
        # whole_salers = company.whole_salers.all()

        # whole_salers = Dealers.objects.select_related('whole_saler').filter(dealer=self.request.user.company)

        # curtains = Curtain.objects.select_related()
        # for i in whole_salers:
        #     print(i.whole_saler)


        curtains_dealers = Curtain.objects.filter(
            brand_company__in=Dealers.objects.values('whole_saler').filter(dealer=self.request.user.company))



        return curtains_dealers
