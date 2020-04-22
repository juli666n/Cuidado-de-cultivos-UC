from django.contrib import admin
from .models import Plant
# Register your models here.


class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    fields = ['name', 'temperature', 'moisture', 'lux', 'isSelected', 'description']


admin.site.register(Plant, PlantAdmin)
