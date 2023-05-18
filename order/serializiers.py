from rest_framework import serializers
from .models import CustomerOrder, DealerOrder
from measurement.serializers import MeasurementSerializer,MeasurementGroupSerializer1
from product.serializers import CurtainSerializer
# class CustomerOrderSerializer(serializers.ModelSerializer):
#     measurement_group = MeasurementGroupSerializer1(read_only=True)
#     # measurement = MeasurementSerializer(read_only=True,)
    
#     class Meta:
#         model = CustomerOrder
#         fields = '__all__'

ORDER_STATUS = (

    ("active", "Aktif"),
    ("preparing", "Hazırlanıyor"),
    ("on_delivery", "Teslimatta"),
    ('delivered', "Teslim Edildi"),
    ('waiting_payment', "Ödeme Bekliyor"),
    ('completed', 'Tamamlandı')
)

class CustomerOrderSerializer(serializers.ModelSerializer):
    measurement_group = serializers.StringRelatedField(read_only=True)
    customer = serializers.StringRelatedField(read_only=False)
    company = serializers.StringRelatedField()
    measurement = MeasurementSerializer(read_only=True,)
    status = serializers.CharField(source= 'get_status_display', read_only=True)
    
    class Meta:
        model = CustomerOrder
        fields = '__all__'


class DealerOrderSerializer(serializers.ModelSerializer):
    unit = serializers.StringRelatedField(read_only=True)
    status = serializers.CharField(source= 'get_status_display', read_only=True)
    dealer_company= serializers.StringRelatedField(read_only=True)
    product_company = serializers.StringRelatedField(read_only=True)
    product = CurtainSerializer(read_only=True)


    class Meta:
        model = DealerOrder
        fields = '__all__'


# {
#     "status": "preparing",
#     "unit_price": 999,
#     "payment": 55,
#     "unit": 1,
#     "product": 1,
#     "dealer_company": 5,
#     "product_company": 4
# }

# {
#     "status": "completed",
#     "unit_price": 1749.99,
#     "payment": 999.99,
#     "unit": 2,
#     "product": 1,
#     "dealer_company": 4,
#     "product_company": 4
# }