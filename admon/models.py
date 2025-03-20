from django.db import models
from catalogo_cuenta.models import catalogo_cuentaModel
from forma_pago.models import FormaPagoModel
from django.contrib.auth.models import User

# Create your models here.

class AdmonBaseModel(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    catalogo_cuenta = models.ForeignKey(catalogo_cuentaModel, on_delete=models.PROTECT, verbose_name='Catalogo cuenta', blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto', blank=False, null=False)
    fecha = models.DateField(verbose_name='Fecha', blank=True, null=True)
    forma_pago = models.ForeignKey(FormaPagoModel, on_delete=models.PROTECT, verbose_name='Forma de Pago', blank=False, null=False)
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario de Creación')
    
    class Meta:
        abstract = True

class IngresoModel(AdmonBaseModel):
    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        db_table = 'ingreso'

class GastoModel(AdmonBaseModel):
    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        db_table = 'gasto'