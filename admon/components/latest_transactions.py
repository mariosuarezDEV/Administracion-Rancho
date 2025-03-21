from django_unicorn.components import UnicornView
from admon.models import IngresoModel, GastoModel
from itertools import chain

class LatestTransactionsView(UnicornView):
    transacciones = []
    count = 0

    def mount(self):
        ingresos = list(IngresoModel.objects.all().order_by('-fecha')[:3])
        gastos = list(GastoModel.objects.all().order_by('-fecha')[:3])
        # Agregamos un atributo personalizado para identificar el tipo
        for ingreso in ingresos:
            ingreso.tipo = "ingreso"
        
        for gasto in gastos:
            gasto.tipo = "gasto"
        # Unir las listas y ordenarlas por fecha
        self.transacciones = sorted(
            chain(ingresos, gastos), key=lambda x: x.fecha, reverse=True
        )
        # Contar el total de transacciones
        self.count = len(self.transacciones)
