from django.contrib import admin
from .models import Brand, Color, Category, Curtain, Unit, CurtainType
# Register your models here.


admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Curtain)
admin.site.register(Unit)
admin.site.register(CurtainType)