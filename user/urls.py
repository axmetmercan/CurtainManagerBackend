from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import UserCRUD, EmployeeTypesViewset


router = routers.DefaultRouter()
router.register(r"employee", UserCRUD, basename='CRUD operations of employees')


router.register(r"types", EmployeeTypesViewset, basename='Lists  of employees types')


urlpatterns = [

    path('', include(router.urls)),

]