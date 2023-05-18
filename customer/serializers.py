from rest_framework import serializers
from .models import Customer
from measurement.serializers import MeasurementGroupSerializer

class CustomerSerializer(serializers.ModelSerializer):
    customer_of = serializers.StringRelatedField(read_only=True)
    measurement_groups = MeasurementGroupSerializer(many=True, required=False, read_only=True)
    class Meta:
        model=Customer
        fields ='__all__'