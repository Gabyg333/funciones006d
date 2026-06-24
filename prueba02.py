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
    elif opcion == 3:
    elif opcion == 4:
    elif opcion == 5:
    elif opcion == 6: