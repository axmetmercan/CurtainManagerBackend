from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import BrandsListView,CurtainListViewSet


router = routers.DefaultRouter()
router.register(r"brands", BrandsListView, basename='Get information of brands')
router.register(r"products", CurtainListViewSet, basename='Get information of products')


urlpatterns = [


    path('', include(router.urls)),

]