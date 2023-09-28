# Sma
# Variables
a = 5
b = 3
Sma = a+b
print(Sma)
# Resta
rest = a-b
print(rest)
# multipli
multi = a*b
print(multi)
# factorizacion elevado
facto = a**b
print(facto)
# division
div = a/b
print(div)
# division Entera Olvida los decimales
div2 = a//b
print(div2)
# modulo aproximacion de acuerdo a los decimales que se tienen numero entero
mod = a % b# devuelve el valor o el resto
print(mod)
# Operador De Asignacion
#Explicacion Dependiendo el tipo de operador este tomara el valor iniciaal actuara el operador y regreseara el resultado
contador = 0
contador -= 1
print(contador)
# Operador De Comparacion "==, != ,<>", comparar datos imprimen falso o verdadero
#Igual
a=5
b=4
resultado = a==b
print(resultado)
#Desigual
result= a != b
print (result)
#Mayor que 
resultad = a>b
print(resultad)
#Menor que
resulta= a<b
print (resulta)
#Mayor o Igual que 
resultad = a >= b
print(resultad)
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