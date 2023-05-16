from rest_framework import serializers
from .models import Picture


class PictureSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Picture
        fields = '__all__'