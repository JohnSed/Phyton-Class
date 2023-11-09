#___________________________________________________
soy_global="Es Es Una Variable"
print(soy_global)
def mi_funcion():
    soy_local="Esta es una variable Local"
    print(soy_local)
    print(soy_global)
mi_funcion()
#__________________
num=3 #Variable Global es pertenece a todo el codigo (Variables Locales)
def Cuadrado():
    global num#La manera de llamar la variable global a mi funcion
    num**=3
Cuadrado()
print(num)

#________Varibales no Locales:Se usa en funciones anidadadasuna funcion dentro deuna funcion padre
def funcion_externa():
    nombre="Marta"
    def funcion_interna():
        nombre="Jose"
        print(nombre)
    print(nombre)
funcion_externa()

def funcion_externa():
    nombre="Marta"
    def funcion_interna():
        nonlocal nombre
        nombre="Jose"
        print(nombre)
    funcion_interna()
    print(nombre)
funcion_externa()
#______________
for i in range(100):
    print(i)
def M(numero):
    if numero ==99:
        print(numero)
    else:
        print(numero)
        M(numero+1)
M(4)
#suma
def sumar(n):
    suma=0
    for i in range(n+1):
        suma+=i
    return suma
print(sumar(4))
#MANERA RECURSICA
def sum2(n):
    if n==1:
        return 1
    else:
        return n+sum2(n-1)
print(sum2(4))