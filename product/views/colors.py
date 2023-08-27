from rest_framework import mixins, viewsets, permissions
from rest_framework.permissions import AllowAny
from ..serializers import ColorSerializer
from ..models import Color
from ..pagination import DefaultPagination
from .tasks import count


class ColorListViewset(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin ):
    
    serializer_class = ColorSerializer
    permission_classes = [AllowAny]
    pagination_class = DefaultPagination

    def get_queryset(self):

        
        count.delay()
        return Color.objects.all()
