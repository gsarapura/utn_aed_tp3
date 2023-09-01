"""
1) Código identificador del ticket (un número entero) [NUEVO].

2) Patente del vehículo al que se le cobra el ticket (una cadena).

3) Tipo de vehículo (un entero entre 0 y 2 - 
(0: motocicleta, 1: automóvil, 2: camión)).

4) Forma de pago 
(un dígito 1 o 2 que indica la forma de pago (1: manual, 2 telepeaje)).

5) País de la cabina 
(un dígito entre 0 y 4 que indica el país donde está la cabina que hizo el cobro 
(0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay)). 

6) Kilómetros recorridos desde la cabina anterior (un entero que puede ser un cero
para indicar que la cabina actual es la primera que ese vehículo atraviesa).
"""

class Ticket:
    def __init__(self, id: int, patente: str, tipo_vehiculo: int, forma_pago: int, pais_cabina: int, distancia_km: int):
        self.id = id
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.distancia_km = distancia_km

    def __str__(self) -> str:
        return f"ID: {self.id}\nPatente: {self.patente}\nTipo de vehiculo: {self.tipo_vehiculo}\nForma de pago: {self.forma_pago}\nPais de la cabina: {self.pais_cabina}\nDistancia en km: {self.distancia_km}"
