from rest_framework import serializers
from product.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Brand
        fields = "__all__"

