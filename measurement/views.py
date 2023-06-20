from rest_framework import viewsets, mixins, permissions
from .models import Room, CurtainModel, MeasurementGroup, Measurement
from .serializers import RoomSerializer, MeasurementSerializer, MeasurementGroupSerializer1, CurtainModelSerializer
from customer.models import Customer
from product.models import Curtain
from .pagination import DefaultPagination

# Create your views here.


class RoomListViewset(viewsets.GenericViewSet,
                      mixins.ListModelMixin):

    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination



class CurtainModelListViewset(viewsets.GenericViewSet,
                              mixins.ListModelMixin):

    serializer_class = CurtainModelSerializer
    queryset = CurtainModel.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination



class MeasurementGroupCRUDViewset(viewsets.ModelViewSet):
    # Usera göre ölçü grubu listeleme eklenecek
    serializer_class = MeasurementGroupSerializer1
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination


    def get_queryset(self):
        measurements = MeasurementGroup.objects.filter(
            company=self.request.user.company, )

        extra_param = self.request.query_params.get('customer_id')        
        if extra_param:
            customer = Customer.objects.get(id=extra_param)
            measurements = MeasurementGroup.objects.filter(
                company=self.request.user.company, customer=customer)
            return measurements
        return measurements

    def perform_create(self, serializer):

        customer = self.request.data.get('customer')  # customer id will given
        company = self.request.user.company
        customer = Customer.objects.get(id=customer)

        instance = serializer.save(
            company=company,
            customer=customer,

        )


class MeasurementListViewset(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             mixins.CreateModelMixin):

    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination


    def get_queryset(self):

        return Measurement.objects.all()
    
    def perform_create(self, serializer):

        measurement_group_id = self.request.data.get('measurement_group_id')
        room_name = self.request.data.get('room_id')
        product = self.request.data.get('product_id')

        instance = serializer.save(

            measurement_group = MeasurementGroup.objects.get(id = measurement_group_id),
            room_name = Room.objects.get(id = room_name),
            product = Curtain.objects.get(id=product),

        )


        return super().perform_create(serializer)
