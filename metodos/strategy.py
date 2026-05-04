from abc import ABC, abstractmethod

# Strategy (interfaz)
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass


# Estrategias concretas
class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando con tarjeta: {monto}")


class PagoPaypal(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando con PayPal: {monto}")


# Contexto
class Carrito:
    def __init__(self, metodo_pago: MetodoPago):
        self.metodo_pago = metodo_pago

    def set_metodo_pago(self, metodo_pago: MetodoPago):
        self.metodo_pago = metodo_pago

    def pagar(self, monto):
        self.metodo_pago.pagar(monto)


# 🧪 Uso
carrito = Carrito(PagoTarjeta())
carrito.pagar(100)

carrito.set_metodo_pago(PagoPaypal())
carrito.pagar(200)