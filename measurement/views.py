from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from .models import Room, CurtainModel, MeasurementGroup, Measurement
from .serializers import RoomSerializer, MeasurementSerializer, MeasurementGroupSerializer, CurtainModelSerializer
from customer.models import Customer
# Create your views here.


class RoomListViewset(viewsets.GenericViewSet,
                      mixins.ListModelMixin):

    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CurtainModelListViewset(viewsets.GenericViewSet,
                              mixins.ListModelMixin):

    serializer_class = CurtainModelSerializer
    queryset = CurtainModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class MeasurementGroupCRUDViewset(viewsets.ModelViewSet):

    serializer_class = MeasurementGroupSerializer
    queryset = MeasurementGroup.objects.all()
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):

        customer = self.request.data.get('customer') #customer id will given
        company = self.request.user.company
        customer = Customer.objects.get(id = customer)

        instance = serializer.save(

            company = company,
            customer = customer,

        )




