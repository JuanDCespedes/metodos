from abc import ABC, abstractmethod

class ProcesoPago(ABC):

    # Template Method (estructura fija)
    def procesar_pago(self, monto):
        self.validar()
        self.calcular(monto)
        self.confirmar()

    def validar(self):
        print("Validando datos...")

    @abstractmethod
    def calcular(self, monto):
        pass

    def confirmar(self):
        print("Confirmando pago...")


# Implementaciones
class PagoTarjetaTM(ProcesoPago):
    def calcular(self, monto):
        print(f"Procesando tarjeta: {monto}")


class PagoPaypalTM(ProcesoPago):
    def calcular(self, monto):
        print(f"Procesando PayPal: {monto}")


# 🧪 Uso
pago = PagoTarjetaTM()
pago.procesar_pago(100)

print("-----")

pago = PagoPaypalTM()
pago.procesar_pago(200)