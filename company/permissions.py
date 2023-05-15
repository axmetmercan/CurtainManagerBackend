from django.forms import ValidationError
from rest_framework import permissions as per

class IsAuthAndBelongsTo(per.BasePermission):

    def has_object_permission(self, request, view, obj):

        isAuth = super().has_object_permission(request, view, obj)
        
        isAuth = (isAuth and (obj.id == request.user))  
        if isAuth or request.method in per.SAFE_METHODS:
            return True
        return False