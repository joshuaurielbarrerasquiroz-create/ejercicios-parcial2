nombre = ""
edad = 0
nacionalidad = ""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")

if edad >= 18:#el if va segido de la condicion y dos puntos
    print("Eres mayor de edad")
else:#el else va seguido de dos puntos para decir que si no se cumple la condicion del if se ejecutara el else
    print("No eres mayor de edad")

    if nacionalidad == "N":
        print("Eres de nacionalidad mexicana")
    else:#el else va seguido de dos puntos para decir que si no se cumple la condicion del if se ejecutara el else
        print("No eres de nacionalidad mexicana")