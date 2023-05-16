from django.urls import path, include
from rest_framework import routers

from .views import RoomListViewset, CurtainModelListViewset,MeasurementGroupCRUDViewset


router = routers.DefaultRouter()
router.register(r"rooms", RoomListViewset, basename='List of available rooms to all')
router.register(r"models", CurtainModelListViewset, basename='List of available curtain models to all')
router.register(r"groups", MeasurementGroupCRUDViewset, basename='List of available measurents of customer')





urlpatterns = [

    path('', include(router.urls)),

]