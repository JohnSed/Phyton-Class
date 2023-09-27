#Estrutctura If simpre separe con coma los datos que desea mostrar
Numero = 2
Numero2 = 2

if Numero > Numero2:
    print("El Numero",Numero, "Es Mayor Que" ,Numero2 )
elif Numero<Numero2:
    print("El Numero",Numero, "Es Menor Que" , Numero2)
else:
    print("El Numero",Numero, "Y el" , Numero2, "Son Iguales")
#While Repite la funcion dada hasta que se cumpla la misma
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
#Estructura For  iterar sobre una secuencia de elementos, como una lista o una cadena
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)
#Estructura For  Con rangos
Numb = 0
for i in range(1, 6):
    print(i)