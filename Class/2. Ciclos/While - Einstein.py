while True:
    #Fmm De La Velocidad m*mc**2
    masa= int(input("Ingrese Masa En Kg: "))
    c= 3000000
    energia= masa *(c**2)
    print ("La energia es igual a: ",energia, "Joules")
    respuesta = input("¿Desea calcular otro IMC? (Sí/No): ").lower()
    if respuesta != 'si':
        break  # Salir del bucle si la respuesta no es 'si'
