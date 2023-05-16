from rest_framework import serializers
from ..models import Curtain


class CurtainSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(read_only=False)
    brand = serializers.StringRelatedField()
    brand_company = serializers.StringRelatedField()
    category = serializers.StringRelatedField()


    


    class Meta:

        model = Curtain
        fields = '__all__'

