# TALLER 5 PHYTON
# AUTOR: JHON SEBASTIAN DIAZ
# FECHA: 9/11/2023
from datetime import date
hoy=date.today()            #Fecha Actual
print("Hoy Es El Dia ",hoy)     #Fecha Actual
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num1=int(input("Digite Primer Numero: "))
num2= int(input("Ingrese Es Segundo Numero (Debe Ser Mayor)"))
print("Ciclos")
for i in range(num1):
    print(i)
print("Fin Del Ciclo")
print()
print("Ciclo Desde el num 1 hasta el num 2")
for i in range(num1,num2):
    print(i)
print("Fin Del Ciclo")
print()
print("Ciclo desde el primer hasta el segundo numero con incrementos de 2 en 2")
for i in range (num1,num2,2):
    print(i)
print("Fin Del Ciclo")
print()
empresa=input("Digite Nombre de una empresa; ")
empresa=empresa.lower()
for caracter in empresa:
    print(caracter)
print("Fin De Ciclo")
print()
print("Fin")
