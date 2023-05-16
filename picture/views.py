from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from .serializers import PictureSerializer
from .models import Picture


class PictureLRViewset(viewsets.GenericViewSet, 
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin):
    
    serializer_class = PictureSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Picture.objects.filter(uploaded_by=self.request.user.company)
    
    def perform_create(self, instance):
        instance.save(uploaded_by=self.request.user.company)
