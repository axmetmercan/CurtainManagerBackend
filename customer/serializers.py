from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    customer_of = serializers.StringRelatedField()
    class Meta:
        model=Customer
        fields ='__all__'