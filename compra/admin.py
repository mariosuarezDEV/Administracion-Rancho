from django.contrib import admin
from unfold.admin import ModelAdmin
# Register your models here.
from .models import CompraModel, det_compraModel

class CompraAdmin(ModelAdmin):
    list_display = [
        'proveedor',
        'monto',
        'fecha',
        'unidad',
        'cantidad',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    search_fields = [
        'proveedor',
        'monto',
        'fecha',
        'unidad',
        'cantidad',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    date_hierarchy = 'fecha'
    list_filter = [
        'proveedor',
        'forma_pago',
        'fecha_creacion',
        'fecha_modificacion',
        'usuario_creacion',
    ]
    list_display_links = ['proveedor']

class DetCompraAdmin(ModelAdmin):
    list_display = [
        'compra', 'precio_unidad', 'subtotal', 'total', 'fecha_modificacion'
    ]
    date_hierarchy = 'fecha_modificacion'
    list_display_links = ['compra']

admin.site.register(det_compraModel, DetCompraAdmin)

admin.site.register(CompraModel, CompraAdmin)
