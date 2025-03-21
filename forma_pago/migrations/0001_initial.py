# Generated by Django 5.1.7 on 2025-03-20 18:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FormaPagoModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(max_length=50, verbose_name="Forma de Pago"),
                ),
                (
                    "descripcion",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "clave_sat",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "Efectivo"),
                            (2, "Cheque nominativo"),
                            (3, "Transferencia electrónica de fondos"),
                            (4, "Tarjeta de crédito"),
                            (5, "Monedero electrónico"),
                            (6, "Dinero electrónico"),
                            (8, "Vales de despensa"),
                            (12, "Dación en pago"),
                            (13, "Pago por subrogación"),
                            (14, "Pago por consignación"),
                            (15, "Condonación"),
                            (17, "Compensación"),
                            (23, "Novación"),
                            (24, "Confusión"),
                            (25, "Remisión de deuda"),
                            (26, "Prescripción o caducidad"),
                            (27, "A satisfacción del acreedor"),
                            (28, "Tarjeta de débito"),
                            (29, "Tarjeta de servicios"),
                            (30, "Aplicación de anticipos"),
                            (31, "Intermediario pagos"),
                            (99, "Por definir"),
                        ],
                        null=True,
                        verbose_name="Clave SAT",
                    ),
                ),
                (
                    "fecha_creacion",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "fecha_modificacion",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de Modificación"
                    ),
                ),
                (
                    "usuario_creacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="usuario_creacion_forma_pago",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuario de Creación",
                    ),
                ),
            ],
            options={
                "verbose_name": "Forma de Pago",
                "verbose_name_plural": "Formas de Pago",
                "db_table": "forma_pago",
            },
        ),
    ]
