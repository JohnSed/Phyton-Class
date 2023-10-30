def Mensaje_Saludo():#Funcion 
    print("Este es un mensaje")#Que hace la funcion

Mensaje_Saludo()#Llamar Funcion
def imprimir_saludo(Nombre):
    """Esto Es una funcion permite imprimir un saludo, Recibe como parametro el nombre del usuario"""#Ingresar un dock string y una detalle de que hace la funcion y se pueda imprimir dentrp de nuestro codigo si lo requerimos
    print (f"Bienvenido Usuario {Nombre}, Como estas?")
    return(f"Bienvenido Usuario {Nombre}")
nombre_usuario = input("Ingrese Nombre: ")
imprimir_saludo(nombre_usuario)
print(imprimir_saludo.__doc__)
def obtener_saludo(Nombre, Apellido):
    saludo=f"Buenas Tardes {Nombre} {Apellido}, Como estas?"
    return saludo
print(obtener_saludo("Juan","Gonzales"))
mi_saludo=obtener_saludo
print(mi_saludo)
def imprimirdespedida(Apellido, Nombre="Luis") :
    print(f"Hasta Luego {Nombre} {Apellido}")
imprimirdespedida("Diaz")