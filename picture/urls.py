from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import PictureLRViewset


router = routers.DefaultRouter()
router.register(r"img", PictureLRViewset, basename='Get information of images')




urlpatterns = [

    path('', include(router.urls)),

]