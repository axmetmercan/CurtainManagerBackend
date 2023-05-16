from rest_framework import serializers
from .models import CurtainModel, Room, Measurement,MeasurementGroup

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class CurtainModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurtainModel
        fields = '__all__'

        
class MeasurementGroupSerializer(serializers.ModelSerializer):

    customer = serializers.StringRelatedField()
    company = serializers.StringRelatedField()

    class Meta:
        model = MeasurementGroup
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):


    class Meta:
        model = Measurement
        fields = '__all__'


