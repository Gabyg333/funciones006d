import uwu as g
#Codigo principal

#Declarar la lista vacia
lista_reservas = []

opcion = 0
while opcion != 6:
    #Mostrar mi menu
    p.mostrar_menu()
    opcion = p.ingresar_opcion()
    if opcion == 1:
        p.agregar_reserva(lista_reservas)
    elif opcion == 2:
        nombre = input("Ingrese el nombre del huesped a buscar: ")
        pos = p.buscar_reserva(lista_reservas, nombre)
        if pos != 1:
            print("***Reserva****")
            print(f"Nombre del huespued: {lista_reservas[pos]["huesped"]}")
            print(f"Numero de habitacion: {lista_reservas[pos]["habitacion"]}")
            print(f"Cantidad de noches: {lista_reservas[pos]["noches"]}")
            estado = "CONFIRMADA" if lista_reservas[pos]["confirmada"] else "PENDIENTE"
            print(f"Estado: {estado}")
            print("**************")
        else:
            print(f"El huesped {nombre} no ha sido encontrado")
    elif opcion == 3:
        nombre = input("Ingrese el nombre del huesped para eliminar la reserva: ")
        pos = p.buscar_reserva(lista_reservas, nombre)
        if pos != -1:
            lista_reservas.pop(pos)
            print("Reserva eliminada")
        else:
            print(f"El huesped {nombre} no ha sido encontrado")
    elif opcion == 4:
        p.confirmar_reservas(lista_reservas)
        print("Reservas actualizadas")
    elif opcion == 5:
        p.confirmar_reservas(lista_reservas)
        p.mostrar_reservas(lista_reservas)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto")
        break