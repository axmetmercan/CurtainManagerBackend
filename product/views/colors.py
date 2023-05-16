from rest_framework import mixins, viewsets, permissions
from ..serializers import ColorSerializer
from ..models import Color

class ColorListViewset(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin ):
    
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = [permissions.IsAuthenticated]