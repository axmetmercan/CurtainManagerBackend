from rest_framework import serializers
from .models import Company, Dealers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DealersSerializer(serializers.ModelSerializer):
    dealer = CompanySerializer()
    class Meta:
        model= Dealers
        fields = '__all__'
        
class CreateDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dealers
        exclude = ['id', 'whole_saler']