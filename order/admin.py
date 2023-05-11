from django.contrib import admin
from .models import CustomerOrder, DealerOrder
# Register your models here.
admin.site.register(CustomerOrder)
admin.site.register(DealerOrder)