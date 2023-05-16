from django.urls import path, include
from rest_framework import routers

from .views import CustomerCRUDViewset


router = routers.DefaultRouter()
router.register(r"customers", CustomerCRUDViewset, basename='CRUD operations of customers')




urlpatterns = [

    path('', include(router.urls)),

]