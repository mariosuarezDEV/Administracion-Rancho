from django.db import models
from proveedor.models import ProveedorModel
from forma_pago.models import FormaPagoModel
from django.contrib.auth.models import User
# Create your models here.

UNIDAD = (
    (1, 'Por animal'),
    (2, 'Por kilo'),
)

class CompraModel(models.Model):
    proveedor = models.ForeignKey(ProveedorModel, on_delete=models.PROTECT, verbose_name='Proveedor', blank=False, null=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Monto', blank=False, null=False)
    fecha = models.DateField(verbose_name='Fecha', blank=True, null=True)
    unidad = models.IntegerField(choices=UNIDAD, verbose_name='Unidad', blank=False, null=False)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cantidad', blank=False, null=False)
    forma_pago = models.ForeignKey(FormaPagoModel, on_delete=models.PROTECT, verbose_name='Forma de Pago', blank=False, null=False)
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario de Creación')
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'compra'
        
class det_compraModel(models.Model):
    compra = models.ForeignKey(CompraModel, on_delete=models.PROTECT, verbose_name='Compra', blank=False, null=False)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio por Unidad', blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal', blank=False, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total', blank=True, null=True)
    total_modificado = models.BooleanField(verbose_name='Total Modificado', blank=True, null=True)
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario de Creación')
    
    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compras'
        db_table = 'det_compra'