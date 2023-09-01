from platform import system
from Ticket import Ticket

def dividir_linea(linea):
    """
    Esta funcion recorta el string de cada linea y devuelve cada tipo de dato.
    :param linea: <str> registro de peaje
    :return: [patente, tipo_vehiculo, forma_de_pago, pais_cabina, distancia]
    """

    id = linea[0:10]
    patente = linea[10:17]
    tipo_vehiculo = linea[17]
    forma_pago = linea[18]
    pais_cabina = linea[19]
    distancia = linea[20:23]

    return int(id), patente, int(tipo_vehiculo), int(forma_pago), int(pais_cabina), int(distancia)

def encontrar_idioma(primera_linea):
    """
    Esta función determina el idioma en base a la primera línea de un registro de peaje.
    :param primera_linea: <str> primera línea del registro de peaje
    :return: <str> idioma encontrado "Portugués", "Español" o "Idioma no encontrado" si no se reconoce
    """

    if "PT" in primera_linea:
        return "Portugués"
    elif "ES" in primera_linea:
        return "Español"
    else:
        return "Idioma no encontrado" 

def crear_arreglo():
    # Chequeo para sistemas Linux - Codificaciones de Windows no válidos para algunos distros de Linux
    ruta_archivo = "peajes-tp3.txt"
    codificacion = "windows-1252" if system() == "Linux" else None

    idioma = None
    v_tickets = []

    archivo = open(ruta_archivo, encoding=codificacion)
    for linea in archivo:
        if idioma == None: 
            idioma = encontrar_idioma(linea)
            continue

        id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km = dividir_linea(linea)

        ticket = Ticket(id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km)
        v_tickets.append(ticket)

    archivo.close()
    
    print("\n", " " * 30, "*" * 3, "Arreglo creado con éxito.", "*" * 3, "\n")


def cargar_ticket():
    pass

def mostrar_registro():
    pass

def buscar_patente_cabina():
    pass
