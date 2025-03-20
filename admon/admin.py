from django.contrib import admin
from unfold.admin import ModelAdmin
# Register your models here.
from .models import IngresoModel, GastoModel

from django.contrib import admin
from unfold.admin import ModelAdmin

class IngresoAdmin(ModelAdmin):
    list_display = [
        'descripcion',
        'catalogo_cuenta',
        'monto',
        'fecha',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    search_fields = [
        'descripcion',
        'catalogo_cuenta',
        'monto',
        'fecha',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    date_hierarchy = 'fecha'
    list_filter = [
        'catalogo_cuenta',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    list_display_links = ['descripcion']

class GastoAdmin(ModelAdmin):
    list_display = [
        'descripcion',
        'catalogo_cuenta',
        'monto',
        'fecha',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    search_fields = [
        'descripcion',
        'catalogo_cuenta',
        'monto',
        'fecha',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    date_hierarchy = 'fecha'
    list_filter = [
        'catalogo_cuenta',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    list_display_links = ['descripcion']
admin.site.register(IngresoModel, IngresoAdmin)
admin.site.register(GastoModel, GastoAdmin)