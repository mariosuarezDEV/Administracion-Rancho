# Generated by Django 5.1.7 on 2025-03-20 19:30

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
            name="ProveedorModel",
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
                    models.CharField(
                        max_length=100, verbose_name="Nombre del proveedor"
                    ),
                ),
                (
                    "psg",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="PSG"
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
                        related_name="proveedor_usuario_creacion",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuario de Creación",
                    ),
                ),
            ],
            options={
                "verbose_name": "Proveedor",
                "verbose_name_plural": "Proveedores",
                "db_table": "proveedor",
            },
        ),
        migrations.CreateModel(
            name="DetProveedorModel",
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
                    "calle",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Calle"
                    ),
                ),
                (
                    "colonia",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Colonia"
                    ),
                ),
                (
                    "cp",
                    models.CharField(
                        blank=True,
                        max_length=5,
                        null=True,
                        verbose_name="Código Postal",
                    ),
                ),
                (
                    "ciudad",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Ciudad"
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Estado"
                    ),
                ),
                (
                    "pais",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="País"
                    ),
                ),
                (
                    "telefono",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Teléfono"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Correo Electrónico",
                    ),
                ),
                (
                    "rfc",
                    models.CharField(
                        blank=True, max_length=13, null=True, verbose_name="RFC"
                    ),
                ),
                (
                    "razon_social",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Razón Social",
                    ),
                ),
                (
                    "uso_cfdi",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Uso CFDI"
                    ),
                ),
                (
                    "banco",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Banco"
                    ),
                ),
                (
                    "clabe",
                    models.CharField(
                        blank=True, max_length=18, null=True, verbose_name="CLABE"
                    ),
                ),
                (
                    "cuenta",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Cuenta"
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
                        related_name="det_proveedor_usuario_creacion",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuario de Creación",
                    ),
                ),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="proveedor.proveedormodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Detalle del Proveedor",
                "verbose_name_plural": "Detalles de los Proveedores",
                "db_table": "det_proveedor",
            },
        ),
    ]
