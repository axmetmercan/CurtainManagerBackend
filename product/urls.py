from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import BrandsListView,CurtainListViewSet, CategoryListViewset, ColorListViewset, MyBrandList


router = routers.DefaultRouter()
router.register(r"brands", BrandsListView, basename='Get information of brands')
router.register(r"mybrands", MyBrandList, basename='Get information of brands')

router.register(r"products", CurtainListViewSet, basename='Get information of products')
router.register(r"products/(?P<code>\w+)/", CurtainListViewSet, basename='Get information of products with code filter')

# router.register(r'variants', CurtainWithVariantViewset, basename='List of available measurents of customer')
# router.register(r'variants/(?P<code>\w+)/', CurtainWithVariantViewset, basename='List of available measurents of customer')
router.register(r"colors", ColorListViewset, basename='Get information of product colors')
router.register(r"categories", CategoryListViewset, basename='Get information of product categories')




urlpatterns = [

    path('', include(router.urls)),

]