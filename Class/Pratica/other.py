# Taller 6 PYTHON
# AUTOR= JHON SEBASTIAN DIAZ
# FECHA: 11/08/2023

from datetime import date
hoy=date.today()        #fecha actual
print("Hoy Es el dia: ",hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print( )
numl=int(input("Digite Un Numero: "))
print("Ciclo Controlaro Por Contador")
i=0
while i <= numl:
    print(i)
    i+=1
print("Final Del Ciclo")
print()
print("Ciclo Controlaro Por Evento")
i=0
Num1=5
Num2= int(input("Digite Un Numero: "))
while Num2 != Num1:
    i+=1
    Num2= int(input("Digite Un Numero: "))
print("Acertaste En El Intento N°", i)
print("Final Del Ciclo")
print()
print("Ciclo Abortado Con La Sentencia Break")
amistad=input("Digite Nombre De Una Amistad: ")
amistad=amistad.upper()
for caracteristicas in amistad:
    print (caracteristicas)
    if caracteristicas== "A":
        break
    print("Fin Ciclo")












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
