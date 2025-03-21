from django_unicorn.components import UnicornView
from admon.models import IngresoModel, GastoModel
from datetime import datetime
class ViewStatsView(UnicornView):
    ingreso = 0
    gasto = 0
    balance = 0
    
    def mount(self):
        mes = datetime.now().month
        print(mes)
        # Obtener todos los ingresos y gastos del mes
        ingresos = IngresoModel.objects.filter(fecha__month=mes)
        gastos = GastoModel.objects.filter(fecha__month=mes)
        self.ingreso = sum([ingreso.monto for ingreso in ingresos])
        self.gasto = sum([gasto.monto for gasto in gastos])
        self.balance = self.ingreso - self.gasto
        # Separar el balance con comas
        self.balance = "{:,}".format(self.balance)
        self.ingreso = "{:,}".format(self.ingreso)
        self.gasto = "{:,}".format(self.gasto)
