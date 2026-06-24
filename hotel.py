def mostrar_menu():
    print("******Menu principal******")
    print("1-. Agregar reserva")
    print("2-. Buscar reserva")
    print("3-. Eliminar reserva")
    print("4-. Confirmar reserva")
    print("5-. Mostrar reserva")
    print("6-. Salir")
    print("************")

def ingresar_opcion():
    while True:
        try:
            op = int(input("Ingrese una opcion: "))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return
        except ValueError:
            print("Ingrese un numero del 1 al 6")