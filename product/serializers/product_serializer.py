from rest_framework import serializers
from ..models import Curtain
from picture.serializers import PictureSerializer


class CurtainSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(read_only=False)
    brand = serializers.StringRelatedField()
    brand_company = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    img1 = PictureSerializer(read_only=True)
    # img2 = serializers.ImageField(required=False)
    # img3 = serializers.ImageField(required=False)

    


    class Meta:

        model = Curtain
        fields = '__all__'

