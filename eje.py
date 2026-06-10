#funciones
def datos_producto(name,stock,price):
    print("*****")
    print(f"* Nombre del producto: {name} *")
    print(f"* Precio del producto: {price} *")
    print(f"* Stock del producto: {stock} *")
    print("*****")

#codigo principal
nombre = input("Ingrese el nombre del producto: ")
while True:
    try:
        precio = int(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Debe ingresar un numero positivo")
        else:
            break
    except ValueError:
        print("Debe escribir un numero valido")
while True:
    try:
        stock = int(input("Ingrese el stock del producto: "))
        if stock < 0:
            print("Debe ser un numero positivo")
        else:
            break
    except ValueError:
        print("Debe escribir un numero valido")

#llamar a la funcion
datos_producto(nombre,stock,precio)#se deben enviar los parametros en el orden inicial: name, stock, price. 