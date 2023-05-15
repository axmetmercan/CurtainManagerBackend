from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import CompanyDetailViews,DealersListViewset, CreateCompanyViewset,CreateDestroyDealerViewset


router = routers.DefaultRouter()
router.register(r"details", CompanyDetailViews, basename='Get information of company')
router.register(r"dealers", DealersListViewset, basename='Get information of dealers')
router.register(r"create", CreateCompanyViewset, basename="Create Company ")
router.register(r"manage/dealer", CreateDestroyDealerViewset, basename="Create Company ")




urlpatterns = [


    path('', include(router.urls)),

]