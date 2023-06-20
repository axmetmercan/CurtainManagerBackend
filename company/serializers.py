from rest_framework import serializers
from .models import Company, Dealers
from picture.serializers import PictureSerializer

class CompanySerializer(serializers.ModelSerializer):
    tax_document_pic = PictureSerializer(read_only=True)
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