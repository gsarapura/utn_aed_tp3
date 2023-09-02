from ticket import *


def principal():
    v_tickets = []

    opc = 0
    while opc != 10:
        print(" ")
        print('-' * 100)
        print(f'{" " * 40}Menu de opciones:')
        print("-" * 100)
        print('\n1. Crear el arreglo de registro desde peajes-tp3.txt')

        print('2. Cargar por teclado los datos de un ticket')

        print('3. Mostrar los registros del arreglo (id de menor a mayor).')

        print('4. Buscar por patente y cabina (se muestra el primero encontrado).')

        print('5. Buscar registro por ticket. Se actualiza la forma de pago y se muestra el registro por pantalla')

        print('6. Mostrar cantidad de vehículos de cada país (incluso \'otro\') que pasaron por las cabinas')

        print('7. Mostrar el importe acumulado por pagos de tickets, por cada uno de los posibles tipos de vehiculo')

        print('8. Según punto 7, mostrar el tipo de vehículo con mayor monto y el porcentaje sobre el monto total.')

        print('9. Mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del arreglo,'
              '\ny cuántos de los vehículos recorrieron una distancia mayor a ese promedio.')

        print('10. Salir\n')

        print("-" * 100)
        opc = int(input('Ingrese su eleccion: '))
        if opc == 1:
            # Falta agregar advertencia si ya hay registros cargados
            # porque "el arreglo debe ser creado de nuevo desde cero"
            v_tickets = crear_arreglo(v_tickets)
        elif opc == 2:
            # Falta validación de cada campo
            # ordenarlos?
            v_tickets = cargar_ticket(v_tickets)
        elif opc == 3:
            # Falta ordenar de menor a mayor (id) por binary search
            mostrar_registros(v_tickets)
        elif opc == 4:
            buscar_patente_cabina(v_tickets)
        elif opc == 5:
            # Mostrar mensaje de no encontrado
            pass
        elif opc == 6:
            pass
        elif opc == 7:
            pass
        elif opc == 8:
            pass
        elif opc == 9:
            distancia(v_tickets)

    if not v_tickets == []:
        for t in v_tickets:
            print(t)


if __name__ == "__main__":
    principal()
