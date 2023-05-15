from rest_framework import serializers
from ..models import Curtain


class CurtainSerializer(serializers.ModelSerializer):

    class Meta:

        model = Curtain
        fields = '__all__'

