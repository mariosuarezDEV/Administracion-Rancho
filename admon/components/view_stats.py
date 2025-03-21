from django_unicorn.components import UnicornView, PollUpdate
from admon.models import IngresoModel, GastoModel
from datetime import datetime
class ViewStatsView(UnicornView):
    ingreso = 0
    gasto = 0
    balance = 0
    mes = datetime.now().month
    
    def mount(self):
        # Obtener todos los ingresos y gastos del mes
        pass
    def update_stats(self):
        # Actualizar los ingresos, gastos y balance
        ingresos = IngresoModel.objects.filter(fecha__month=self.mes)
        gastos = GastoModel.objects.filter(fecha__month=self.mes)
        self.ingreso = sum([ingreso.monto for ingreso in ingresos])
        self.gasto = sum([gasto.monto for gasto in gastos])
        self.balance = self.ingreso - self.gasto
        # Separar el balance con comas
        self.balance = "{:,}".format(self.balance)
        self.ingreso = "{:,}".format(self.ingreso)
        self.gasto = "{:,}".format(self.gasto)
    
    def get_stats(self):
        self.update_stats()
        return PollUpdate(timing=2000, disable=False, method="get_stats")
