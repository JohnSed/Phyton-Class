lista=[1,-8,-3,8,15,10]
multiplicacion_pares=1
suma_impares=0

for i in lista:
    if i % 2 == 0: 
        multiplicacion_pares *= i
    else:  
        suma_impares += i

print(suma_impares)
print(multiplicacion_pares)
#______________________________________________
lista=['HTML', "",'CSS', 'jQuery', 'Angular', 'Zend', 'Angular', 'PHP', 'Ruby', 'C#']
valor_anterior=""
valor_nuevo=""
for i in range(len(lista)):
    if lista [i]==valor_anterior:
        lista[i]=valor_nuevo
print(valor_nuevo)


#____________________________________________________
listap=["Htmal","Phyton","","Java"]
nueva_lista = [elemento for elemento in listap if elemento.strip() != ""]
print(nueva_lista)
print(max(2,8))
print(max(7,6,5))

Verificacion=str(input("Es Usted Mayor De Edad (Si) (No): "))
nuevaverificaion=Verificacion.lower()#VOLVER MI INPUT EEN MINUSCULA Y PARA 
if nuevaverificaion == "si":
    while True:
         Nombre=str(input("Ingrese Su Nombre"))
         Phone=int(input("Ingrese Numero Celular"))
         Lista=list[input("Ingrese Lista")]
         if Nombre =="" and Phone=="":
              print("Formulario Vacio Por Favor  Llenar")


    