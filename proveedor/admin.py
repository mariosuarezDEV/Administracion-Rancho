from django.contrib import admin
from unfold.admin import ModelAdmin
# Register your models here.
from .models import DetProveedorModel, ProveedorModel

class ProveedorAdmin(ModelAdmin):
    list_display = ['id', 'nombre', 'psg', 'fecha_modificacion']
    search_fields = ['nombre', 'psg']
    date_hierarchy = 'fecha_modificacion'
    list_display_links = ['nombre']

    def __str__(self):
        return self.nombre

class DetProveedorAdmin(ModelAdmin):
    list_display = ['id', 'proveedor', 'fecha_modificacion']
    search_fields = ['proveedor']
    date_hierarchy = 'fecha_modificacion'
    list_display_links = ['proveedor']

    def __str__(self):
        return self.proveedor

admin.site.register(ProveedorModel, ProveedorAdmin)
admin.site.register(DetProveedorModel, DetProveedorAdmin)