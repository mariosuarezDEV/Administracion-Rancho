from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  catalogo_cuentaModel(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombre', blank=False, null=False)
    codigo_agrupador = models.CharField(max_length=50, verbose_name='codigo agrupador', blank=False, null=False)
    nivel = models.IntegerField( verbose_name='nivel', blank=False, null=False)
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario_creacion_catalogo_cuenta', verbose_name='Usuario de Creación')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Catalogo de Cuenta'
        verbose_name_plural = 'Catalogo de Cuentas'
        db_table = 'catalogo_cuenta'