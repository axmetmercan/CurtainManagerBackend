from django.contrib import admin
from .models import Measurement, Room, CurtainModel

# Register your models here.

admin.site.register(Measurement)
admin.site.register(Room)
admin.site.register(CurtainModel)