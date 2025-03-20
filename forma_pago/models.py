from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Ref: https://xpd.mx/blog/catalogo-de-forma-de-pago-para-cfdi-4-0-claves-actualizadas.html
CLAVE_SAT = (
    (1, 'Efectivo'),
    (2, 'Cheque nominativo'),
    (3, 'Transferencia electrónica de fondos'),
    (4, 'Tarjeta de crédito'),
    (5, 'Monedero electrónico'),
    (6, 'Dinero electrónico'),
    (8, 'Vales de despensa'),
    (12, 'Dación en pago'),
    (13, 'Pago por subrogación'),
    (14, 'Pago por consignación'),
    (15, 'Condonación'),
    (17, 'Compensación'),
    (23, 'Novación'),
    (24, 'Confusión'),
    (25, 'Remisión de deuda'),
    (26, 'Prescripción o caducidad'),
    (27, 'A satisfacción del acreedor'),
    (28, 'Tarjeta de débito'),
    (29, 'Tarjeta de servicios'),
    (30, 'Aplicación de anticipos'),
    (31, 'Intermediario pagos'),
    (99, 'Por definir'),
)

class FormaPagoModel(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Forma de Pago', blank=False, null=False)
    descripcion = models.CharField(max_length=255, verbose_name='Descripción', blank=True, null=True)
    clave_sat = models.IntegerField(choices=CLAVE_SAT, verbose_name='Clave SAT', blank=True, null=True)
    # Auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')
    usuario_creacion = models.ForeignKey(User, on_delete=models.PROTECT, related_name='usuario_creacion_forma_pago', verbose_name='Usuario de Creación')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de Pago'
        db_table = 'forma_pago'