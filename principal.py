from ticket import *


def principal():
    v_tickets = []
    v_acumulador_importe = []
    v_registro_id_manual = []
    opc = "0"

    while opc != "10":
        print(" ")
        print("-" * 100)
        print(f'{" " * 40}Menú de opciones:')
        print("-" * 100)
        print("\n1. Crear el arreglo de registro desde peajes-tp3.txt")

        print("2. Cargar por teclado los datos de un ticket")

        print("3. Mostrar los registros del arreglo (id de menor a mayor).")

        print("4. Buscar por patente y cabina (se muestra el primero encontrado).")

        print("5. Buscar por ID (código). Se cambia la forma de pago y se muestra el registro por pantalla")

        print("6. Mostrar cantidad de vehículos de cada país (incluso \'otro\') que pasaron por las cabinas")

        print("7. Mostrar el importe acumulado por pagos de tickets, por cada uno de los posibles tipos de vehiculo")

        print("8. Según punto 7, mostrar el tipo de vehículo con mayor monto y el porcentaje sobre el monto total.")

        print("9. Mostrar la distancia promedio desde la última cabina recorrida y cantidad de vehículos que "
              "\nrecorrieron una distancia mayor al promedio.")

        print("10. Salir\n")

        print("-" * 100)
        opc = input("Ingrese su elección: ")

        if opc == '1':
            if not v_tickets:
                v_tickets = crear_arreglo()
            else:
                op = input("\n* Advertencia: se borrarán los registros hechos * \n1 Continuar - 0 Volver: ")

                while op not in "0 1":
                    op = input("1 Continuar - 0 Volver: ")

                if op == "1":
                    v_tickets = crear_arreglo()
                else:
                    continue
        elif opc == "2":
            cargar_ticket(v_tickets, v_registro_id_manual)
        elif opc == "3":
            mostrar_registros(v_tickets)
        elif opc == "4":
            buscar_patente_cabina(v_tickets)
        elif opc == "5":
            buscar_registro_id(v_tickets)
        elif opc == "6":
            mostrar_cantidad_patentes(v_tickets)
        elif opc == "7":
            v_acumulador_importe = mostrar_acumulado_por_vehiculo(v_tickets)
        elif opc == "8":
            mostrar_mayor_porcentaje(v_acumulador_importe)
        elif opc == "9":
            mostrar_distancia(v_tickets)
        elif opc != "10":
            print("\n", " " * 29, "-" * 3, "Ingrese una opción correcta.", "-" * 3)


if __name__ == "__main__":
    principal()
