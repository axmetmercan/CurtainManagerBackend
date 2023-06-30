from django.urls import path, include
from rest_framework import routers

from .views import CustomerOrderListViewset, DealerOrderListViewset


router = routers.DefaultRouter()
router.register(r"customer/details", CustomerOrderListViewset, basename='List of available order details belongs that company')
router.register(r'customer/details/(?P<group>\w+)/', CustomerOrderListViewset, basename='List of available order detail of custome1r')
router.register(r'customer/details/(?P<group>\w+)/(?P<company>\w+)/', CustomerOrderListViewset, basename='List of available order detail of custome1r')

router.register(r"dealer/details", DealerOrderListViewset, basename='List of available order details of that company dealers')
router.register(r'dealer/details/(?P<group>\w+)/', DealerOrderListViewset, basename='List of  order details of that company dealers')



urlpatterns = [

    path('', include(router.urls)),

]