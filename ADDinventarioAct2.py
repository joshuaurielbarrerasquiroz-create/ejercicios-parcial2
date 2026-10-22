nombreDeObjeto = "papilla"#aqui va el nombre del objeto
cantidadDeObjeto = 50#aqui va la cantidad del objeto
tipoDeObjeto = "comida"#aqui va el tipo del objeto
precioDeObjeto = 70.0#aqui va el precio del objeto
codigoDeObjeto = 122121#aqui va el id del objeto

print("ingrese el nombre del objeto")
nombreDeObjeto=input("papilla")
print("ingrese la cantidad del objeto")
cantidadDeObjeto=int(input("50"))
print("ingrese el tipo del objeto")
tipoDeObjeto=input("comida")
print("ingrese el precio del objeto")
precioDeObjeto=float(input("70.0"))
print("ingrese el codigo del objeto")
codigoDeObjeto=int(input("122121"))

if cantidadDeObjeto >= 2:#el if va segido de la condicion y dos puntos
    print("no hay suficiente cantidad de",nombreDeObjeto)
    