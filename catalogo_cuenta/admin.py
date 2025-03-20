from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.
from .models import catalogo_cuentaModel

class catalogo_cuentaAdmin(ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'codigo_agrupador',
        'nivel',
        'fecha_modificacion',
    ]
    search_fields = [
        'nombre',
        'codigo_agrupador',
    ]
    date_hierarchy = 'fecha_modificacion'
    list_filter = [
        'nivel',
    ]
    list_display_links = [
        'nombre',
    ]

admin.site.register(catalogo_cuentaModel, catalogo_cuentaAdmin)