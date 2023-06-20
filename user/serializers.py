from rest_framework import serializers
from .models import User
from .models import UserType


class UserSerializer(serializers.ModelSerializer):
    
    type = serializers.StringRelatedField(read_only=True)
    company = serializers.StringRelatedField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    class Meta:
        model = User
        # fields='__all__'
        exclude = ['is_active', 'is_staff',  'is_superuser', 'groups', 'user_permissions','is_deleted','password']


class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserType
        fields='__all__'