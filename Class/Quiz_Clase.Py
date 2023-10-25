numero1=9
numero2=5
numero3=1
if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
else:
    print(numero3)
#---------------------
#Dado un número cualquiera (asignado de antemano a la variable ya existente numero), escriba un programa que en caso de que dicho número sea par, imprima exactamente el mensaje El número ingresado es par, y que en caso contrario, imprima el mensaje El número ingresado es impar.
numero=5
if numero % 2==0:
    print("par")
else:
    print("impar")

    print(numero%2)

#__________________________________________
caracter="P"
caracter= caracter.lower()
vocales=["a","e","i","o","u"]
if caracter in vocales:
    print("es vocal")
else:
    print("no es vocal")
#___________________________________________
anio=400
if anio % 4 ==0:
    print("El Año Ingresado Es Bisiest")
else:
    print("El año no es bisiesto")
#________________________________________
nota= 4.9

if nota < 0 or nota > 5:
    print("Nota Invalida, Por Favor Ingrese Nueva Nota")
elif nota >= 0 and nota < 2:
    print("Nota Deficiente")
elif nota >= 2 and nota < 3:
    print("Nota Insuficiente")
elif nota >= 3 and nota < 4.5:
    print("Nota Aceptable")
elif nota >= 4.5 and nota < 5:
    print("Nota Sobresaliente")
#__________________________________________
angulo_1=0
angulo_2=180
angulo_3=0
if angulo_1+angulo_2+angulo_3==180 and angulo_1 > 0 and angulo_2 > 0 and angulo_3 > 0:
    print("Es un triángulo válido")
else:
    print("NO es un triángulo válido")