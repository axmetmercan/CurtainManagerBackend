from rest_framework import mixins, viewsets, permissions
from ..serializers import ColorSerializer
from ..models import Color
from ..pagination import DefaultPagination


class ColorListViewset(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin ):
    
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
