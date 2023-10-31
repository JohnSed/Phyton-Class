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

#________Varibales no Locales:Se usa en funciones anidadadas
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
    funcion_externa()
    print(nombre)
funcion_externa()