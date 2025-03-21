from django_unicorn.components import UnicornView,PollUpdate
from admon.models import IngresoModel, GastoModel
from itertools import chain
from django.utils.timezone import now

class LatestTransactionsView(UnicornView):
    polling_disabled = False
    transacciones = []
    count = 0

    def mount(self):
        """Carga inicial de transacciones al montar el componente."""
        self.update_transactions()

    def update_transactions(self):
        """Carga y actualiza la lista de transacciones."""
        ingresos = list(IngresoModel.objects.all().order_by('-fecha')[:3])
        gastos = list(GastoModel.objects.all().order_by('-fecha')[:3])

        for ingreso in ingresos:
            ingreso.tipo = "ingreso"

        for gasto in gastos:
            gasto.tipo = "gasto"

        self.transacciones = sorted(
            chain(ingresos, gastos), key=lambda x: x.fecha, reverse=True
        )
        self.count = len(self.transacciones)

    def get_transactions(self):
        """Método que se ejecuta cada 2 segundos para actualizar la vista."""
        self.update_transactions()
        return PollUpdate(timing=2000, disable=False, method="get_transactions")
