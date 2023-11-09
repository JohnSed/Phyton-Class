cadena= "Tesla es una cadena de carros electrico y compiete con Tiviar, Ford y BMW"
print(cadena.count("a")) #Contador Las cadenas son lista de caracteres
print(cadena.find("Ford"))
print(cadena.find("a",10))
print(cadena.replace("e","x"))#remplaza la caracteristica que deseo porotra que elija
print(cadena.replace("Tesla","Mazda"))#remplaza la caracteristica que deseo porotra que elija 
#Estas no modifican la cadena original
print(cadena.split())#separar mi cadena
print(cadena.split("e"))#separar mi cadena por un caracter
#Condicionales and, or  & not
Nm1 = float(input("Ingrese el primer número: "))
Nm2 = float(input("Ingrese el segundo número: "))
#Usar el and cuando deseo que se cumplan mas de una condicion
if Nm1 > Nm2 and Nm2 < 10:
    print("El número", Nm1, "es mayor que", Nm2, "y menor que 10.")
else:
    print("El número", Nm1, "no es mayor que", Nm2, "o", Nm2, "no es menor que 10.")
nombre= "Juan David"
print(id(nombre))
MiNombre= nombre
print(id(MiNombre))
print(nombre is MiNombre) # Aqui SE TOMA UN TRUE PORUE EL VALOR DE LA VARIABLE ES LA MISMA.
