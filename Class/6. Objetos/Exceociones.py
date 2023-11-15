personas = {123: "Juan", 456: "Pedro", 789: "sumadre"}

while True:
    try:
        cedula = int(input("Ingrese Numero De Cedula: "))  # Siempre Debe estar dentro del try
        print(personas[cedula])
    except KeyError:
        print("Cedula No Registrada, Ingrese De NUEVO")
    except (ValueError, TypeError):
        print("Error De Ingreso De Cedula. Por favor, ingrese un número válido.")

    intentar_nuevo = True  # Flag to control the outer loop

    while True:
        respuesta = input("¿Desea Intentar De Nuevo? (Sí/No): ").lower()
        if respuesta == 'si' or respuesta == 'no':
            break
        

    if respuesta == 'no':
        intentar_nuevo = False
        break  # Salir del bucle principal si la respuesta es 'no'

    if not intentar_nuevo:
        break  # Salir del bucle principal si el flag es False

print("Fin Del Programa")