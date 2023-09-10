from platform import system


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
    patente = linea[11:17] if linea[10] == " " else linea[10:17]
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


def crear_arreglo():
    # Chequeo para sistemas Linux - Codificaciones de Windows no válidos para algunos distros de Linux
    ruta_archivo = "peajes-tp3.txt"
    cod = "windows-1252" if system() == "Linux" else None

    v_tickets = []

    idioma = None

    archivo = open(ruta_archivo, encoding=cod)
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
def crear_rango(comienzo, final):
    rango = []
    for i in range(comienzo, final + 1):
        rango.append(str(i))

    return rango


def validar_rango(comienzo, final, mensaje):
    op = input(f"\n{mensaje}")
    rango = crear_rango(comienzo, final)

    while op not in rango:
        op = input(f"Por favor, ingrese un entero entre {comienzo} y {final}: ")

    return int(op)


def cargar_entero_valido(mensaje):
    op = input(f"\n{mensaje}")

    while not op.isnumeric():
        op = input("Por favor, ingrese un entero: ")

    return int(op)


def cargar_ticket(v_tickets):
    print("\nCargar ticket:")

    # Ingresar ID, no importa qué cantidad tenga
    registro_id = cargar_entero_valido("\nIngrese el ID:")

    # No haría faltar verificar porque si no se reconoce, es "otro".
    patente = input("\nIngrese la patente: ")

    tipo_vehiculo = validar_rango(0, 2, "Ingrese tipo de vehiculo (0: motocicleta, 1: automóvil, 2: camión): ")
    forma_pago = validar_rango(1, 2, "Ingrese forma de pago (1: manual, 2 telepeaje): ")
    pais_cabina = validar_rango(0, 4, "Ingrese país de la cabina (0: : Argentina - "
                                      "1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")

    # Valor mayor a tres dígitos
    distancia_km = cargar_entero_valido("Ingrese los kilómetros recorridos desde la cabina anterior "
                                        "(0 si es la primera): ")

    ticket = Ticket(registro_id, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia_km)
    v_tickets.append(ticket)

    print("\n", " " * 30, "*" * 3, "Registro cargado con éxito.", "*" * 3)


# Punto 3
def ordenar_ascendente_dir(v_tickets):
    largo = len(v_tickets)

    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if v_tickets[i].registro_id > v_tickets[j].registro_id:
                v_tickets[i], v_tickets[j] = v_tickets[j], v_tickets[i]


def ordenar_ascendente_bin(v_tickets):
    pass


def mostrar_registros(v_tickets):
    if not v_tickets:
        print("\nNo hay registros.")
    else:
        ordenar_ascendente_dir(v_tickets)
        for t in v_tickets:
            print(f"\n{t}")


# Punto 4
def buscar_patente_cabina(v_tickets):
    if not v_tickets:
        print("\nNo hay registros.")
        return

    print("\nBúsqueda:")

    patente = input("Ingrese la patente (string): ")
    pais_cabina = validar_rango(0, 4, "Ingrese país de la cabina (0: : Argentina - "
                                      "1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")
    # Búsqueda secuencial
    for t in v_tickets:
        if t.patente == patente and t.pais_cabina == pais_cabina:
            print("\nPatente encontrada:")
            print(t)
            return

    # Búsqueda binaria: requiere tener lista ordenada
    izq, der = 0, len(v_tickets) - 1

    print("\n", " " * 30, "-" * 3, "Sin resultado disponible.", "-" * 3)


def acumulado_por_cabina(v):
    acumulador = [0] * 15
    cant = [0] * 15

    for vehiculo in v:
        pos = vehiculo.cabina
        acumulador[pos] += vehiculo.importe
        cant[pos] += 1

def distancia(tickets):
    suma = 0
    for ticket in tickets:
        suma += ticket.distancia_km
    promedio = suma / len(tickets)

    contador = 0
    for ticket in tickets:
        if float(ticket.distancia_km) >= promedio:
            contador += 1
            
    print("Promedio de distancias recorridas: ", promedio)
    print("Cantidad de vehiculos que supera el promedio: ", contador)


# Encontrar patente cargada por usuario


def buscar_patente(v, p):
    apariciones = []
    for vehiculo in v:
        if vehiculo.patente == p:
            apariciones.append(vehiculo)

    return apariciones

