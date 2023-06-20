from rest_framework import serializers
from .models import CurtainModel, Room, Measurement, MeasurementGroup
from product.serializers import CurtainSerializer

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class CurtainModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurtainModel
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    measurement_group = serializers.StringRelatedField(read_only=False)
    room_name = serializers.StringRelatedField(read_only=False)
    product = CurtainSerializer(required=False, read_only=True)
    class Meta:
        model = Measurement
        fields = '__all__'


class MeasurementGroupSerializer(serializers.ModelSerializer):

    customer = serializers.StringRelatedField()
    company = serializers.StringRelatedField()
    # measurementsasd = MeasurementSerializer(many=True, read_only=True, required=False)
    # measurements=MeasurementSerializer(many=True)
    class Meta:
        model = MeasurementGroup
        fields = '__all__'


class MeasurementGroupSerializer1(serializers.ModelSerializer):

    # customer = serializers.StringRelatedField(read_only=True)
    company = serializers.StringRelatedField(read_only=True)
    measurements= MeasurementSerializer (many=True, read_only=True)
    class Meta:
        model = MeasurementGroup
        fields = '__all__'
