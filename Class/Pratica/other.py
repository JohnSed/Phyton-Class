# Taller 4 PYTHON
# AUTOR= JHON SEBASTIAN DIAZ
# FECHA: 11/08/2023

from datetime import date
hoy=date.today()        #fecha actual
print("Hoy Es el dia: ",hoy)
print()
print("EJERICIO DE LA CALSE TRIANGULOS")
a=int(input("Digite valor de a: "))
b=int(input("Digite valor de b: "))
c=int(input("Digite valor de c: "))
if a==b and a==c and b==c:
    print("El Triangulo Es Equilatero")
else:
    if a==b or b==c or a==c:
        print("El Triangulo Es Isoceles")
    else:
        print("El Triangulo Es Escalonado")
print()
animal=input("Ingrese el animar: ")
animal = animal.upper()
if animal =="PERRO":
    print("Este Animal es el mejor amigo del hombre ", animal)
elif animal=="GATO":
    print("Este Animal persigue a los ratones ", animal)
elif animal=="OSO":
    print("Este Animal Vive En El Polo Norte ", animal)
else:
    print("El animal ingresado no es perro, gato ni oes es: ", animal)
print()
print("FIN")
