from django_unicorn.components import UnicornView


class AddGastoView(UnicornView):
    descripcion = "Descripción del gasto"
    monto = 0
