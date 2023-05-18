from rest_framework import mixins, viewsets, permissions
from ..serializers import CategorySerializer
from ..models import Category
from ..pagination import DefaultPagination


class CategoryListViewset(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin ):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
