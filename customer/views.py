from rest_framework import viewsets, permissions
from .models import Customer
from .serializers import CustomerSerializer
from .pagination import DefaultPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from CurtainManager.utils import delete_cache


# Create your views here.


class CustomerCRUDViewset(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = DefaultPagination
    CACHE_KEY_PREFIX = 'customer-crud'

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60*60, key_prefix=CACHE_KEY_PREFIX))
    def dispatch(self, request, *args, **kwargs):
        return super(CustomerCRUDViewset, self).dispatch(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def get_queryset(self):

        return Customer.objects.filter(customer_of=self.request.user.company)

    def perform_create(self, serializer):

        instance = serializer.save(

            customer_of=self.request.user.company,
        )

        return super().perform_create(serializer)
