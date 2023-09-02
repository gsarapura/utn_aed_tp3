from platform import system

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
    def __init__(self, registro_id: int, patente: str, tipo_vehiculo: int, forma_pago: int, pais_cabina: int,
                 distancia_km: int):
        self.registro_id = registro_id
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.distancia_km = distancia_km

    def __str__(self) -> str:
        return f"ID: {self.registro_id}\nPatente: {self.patente}\nTipo de vehiculo: {self.tipo_vehiculo}" \
               f"\nForma de pago: {self.forma_pago}\nPais de la cabina: {self.pais_cabina}\nDistancia en km: " \
               f"{self.distancia_km}"


# Punto 1
def dividir_linea(linea):
    """
    Esta función recorta el string de cada línea y devuelve cada tipo de dato.
    :param linea: <str> registro de peaje
    :return: [patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia]
    """

    registro_id = linea[0:10]
    # Eliminar espacios solo para las que tienen espacios
    patente = linea[10:17].strip()
    tipo_vehiculo = linea[17]
    forma_pago = linea[18]
    pais_cabina = linea[19]
    distancia = linea[20:23]

    return int(registro_id), patente, int(tipo_vehiculo), int(forma_pago), int(pais_cabina), int(distancia)


def encontrar_idioma(primera_linea):
    """
    Esta función determina el idioma según la primera línea de un registro de peaje.
    :param primera_linea: <str> primera línea del registro de peaje
    :return: <str> idioma encontrado "Portugués", "Español" o "Idioma no encontrado" si no se reconoce
    """

    if "PT" in primera_linea:
        return "Portugués"
    elif "ES" in primera_linea:
        return "Español"
    else:
        return "Idioma no encontrado"


def crear_arreglo(v_tickets):
    # Chequeo para sistemas Linux - Codificaciones de Windows no válidos para algunos distros de Linux
    ruta_archivo = "peajes-tp3.txt"
    codificacion = "windows-1252" if system() == "Linux" else None

    v_tickets = []

    idioma = None

    archivo = open(ruta_archivo, encoding=codificacion)
    for linea in archivo:
        if idioma is None:
            idioma = encontrar_idioma(linea)
            continue

        registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km = dividir_linea(linea)

        ticket = Ticket(registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km)
        v_tickets.append(ticket)

    archivo.close()

    print("\n", " " * 30, "*" * 3, "Arreglo creado con éxito.", "*" * 3)

    return v_tickets


# Punto 2
def cargar_ticket(v_tickets):
    print("\nCargar ticket:")

    id = int(input("Ingrese el id (entero): "))
    patente = input("Ingrese la patente (string): ")
    tipo_vehiculo = int(
        input("Ingrese el tipo de vehículo (un entero entre 0 y 2 - (0: motocicleta, 1: automóvil, 2: camión)): "))
    forma_pago = int(
        input("Ingrese la forma de pago (un dígito 1 o 2 que indica la forma de pago (1: manual, 2 telepeaje)): "))
    pais_cabina = int(input(
        "Ingrese el país de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay)): "))
    distancia_km = int(input(
        "Ingrese los kilómetros recorridos desde la cabina anterior (0 si es la primera): "))

    ticket = Ticket(id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km)
    v_tickets.append(ticket)

    print("\n", " " * 30, "*" * 3, "Registro cargado con éxito.", "*" * 3)

    return v_tickets


# Punto 3
def mostrar_registros(v_tickets):
    if not v_tickets:
        print("\nNo hay registros.")
    else:
        for t in v_tickets:
            print(" ")
            print(t)


# Punto 4
def buscar_patente_cabina(v_tickets):
    if not v_tickets:
        print("\nNo hay registros.")
        return None

    print("\nBúsqueda:")

    patente = input("Ingrese la patente (string): ")
    pais_cabina = int(input(
        "Ingrese el país de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay)): "))

    for t in v_tickets:
        if t.patente == patente and t.pais_cabina == pais_cabina:
            print("\nPatente encontrada:")
            print(t)
            return None

    print("\n", " " * 30, "-" * 3, "Sin resultado disponible.", "-" * 3)


def acumulado_por_cabina(v):
    acumulador = [0] * 15
    cant = [0] * 15

    for vehiculo in v:
        pos = vehiculo.cabina
        acumulador[pos] += vehiculo.importe
        cant[pos] += 1


# Encontrar patente cargada por usuario