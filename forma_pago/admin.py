from django.contrib import admin
from unfold.admin import ModelAdmin
# Register your models here.
from .models import FormaPagoModel

class FormaPagoAdmin(ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'descripcion',
        'clave_sat',
        'fecha_modificacion'
    ]
    search_fields = [
        'nombre',
        'descripcion',
        'clave_sat'
    ]
    list_filter = [
        'clave_sat'
    ]
    date_hierarchy = 'fecha_modificacion'
    list_display_links = ['nombre']
    
admin.site.register(FormaPagoModel, FormaPagoAdmin)

