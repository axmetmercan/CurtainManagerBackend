from django.contrib import admin
from .models import Measurement, Room, CurtainModel, MeasurementGroup

# Register your models here.

admin.site.register(Measurement)
admin.site.register(Room)
admin.site.register(CurtainModel)
admin.site.register(MeasurementGroup)