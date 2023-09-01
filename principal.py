# from Ticket import Ticket
from funciones import *

def principal():
    opc = 0
    while opc != 10:
        print('-' * 100)
        print(f'{" " * 40}Menu de opciones:')
        print("-" * 100)
        print('\n1. Crear el arreglo de registro desde peajes-tp3.txt')

        print('2. Cargar por teclado los datos de un ticket')

        print('3. Mostrar los registros del arreglo (id de menor a mayor).')

        print('4. Buscar por patente y cabina.')

        print('5. Buscar si existe en el arreglo un registro cuyo código de ticket sea igual a c, siendo c una valor que se carga por teclado. Si existe, cambiar el valor del campo forma de pago, de forma que pase a valer el valor contrario (si valía 1, que pase a valer 2, y viceversa), y luego mostrar el registro completo modificado. Si no existe indicar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el criterio pedido.')

        print('6. Determinar la cantidad de vehículos de cada país que pasaron por las cabinas, contando también los vehículos que no son de ninguno de los siete paises básicos.')

        print('7. Determinar el importe acumulado por pagos de tickets, por cada uno de los posibles tipos de vehiculo (un acumulador por cada uno de los tres tipos).')
        print('8. En base al resultado obtenido en el punto 7, determinar y mostrar cuál fue cuál fue el tipo de vehículo con mayor monto acumulado, e indicar además qué porcentaje representa ese monto mayor sobre el monto total.')

        print('9. Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del arreglo, e informar además cuántos de los vehículos recorrieron una distancia mayor a ese promedio.')

        print('10. Salir\n')

        print("-" * 100)
        opc = int(input('Ingrese su eleccion: '))
        if opc == 1:
            crear_arreglo()
        elif opc == 2:
            cargar_ticket()
        elif opc == 3:
            mostrar_registro()
        elif opc == 4:
            buscar_patente_cabina()
        elif opc == 5:
            pass
        elif opc == 6:
            pass
        elif opc == 7:
            pass
        elif opc == 8:
            pass
        elif opc == 9:
            pass

if __name__ == "__main__":
    principal()
