from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProveedorModel(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del proveedor', blank=False, null=False)
    psg = models.CharField(max_length=100, verbose_name='PSG', blank=True, null=True)
    # Auditoría
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='proveedor_usuario_creacion', verbose_name='Usuario de Creación')
    
    def __str__(self):
        return f'{self.nombre} - {self.psg}'
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'

class DetProveedorModel(models.Model):
    proveedor = models.ForeignKey(ProveedorModel, on_delete=models.CASCADE)
    # Dirección
    calle = models.CharField(max_length=100, verbose_name='Calle', blank=True, null=True)
    colonia = models.CharField(max_length=100, verbose_name='Colonia', blank=True, null=True)
    cp = models.CharField(max_length=5, verbose_name='Código Postal', blank=True, null=True)
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad', blank=True, null=True)
    estado = models.CharField(max_length=100, verbose_name='Estado', blank=True, null=True)
    pais = models.CharField(max_length=100, verbose_name='País', blank=True, null=True)
    # Contacto
    telefono = models.CharField(max_length=10, verbose_name='Teléfono', blank=True, null=True)
    email = models.EmailField(verbose_name='Correo Electrónico', blank=True, null=True)
    # Datos Fiscales
    rfc = models.CharField(max_length=13, verbose_name='RFC', blank=True, null=True)
    razon_social = models.CharField(max_length=100, verbose_name='Razón Social', blank=True, null=True)
    uso_cfdi = models.CharField(max_length=100, verbose_name='Uso CFDI', blank=True, null=True)
    # Datos Bancarios
    banco = models.CharField(max_length=100, verbose_name='Banco', blank=True, null=True)
    clabe = models.CharField(max_length=18, verbose_name='CLABE', blank=True, null=True)
    cuenta = models.CharField(max_length=20, verbose_name='Cuenta', blank=True, null=True)
    # Auditoría
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='det_proveedor_usuario_creacion', verbose_name='Usuario de Creación')
    def __str__(self):
        return f'{self.proveedor.nombre} - {self.proveedor.psg}'
    
    class Meta:
        verbose_name = 'Detalle del Proveedor'
        verbose_name_plural = 'Detalles de los Proveedores'
        db_table = 'det_proveedor'