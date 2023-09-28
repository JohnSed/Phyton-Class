while True: # bucle while es una estructura de control en programación que permite ejecutar un bloque de código repetidamente mientras una condición dada sea verdadera
        peso = float(input("Introducir su peso en kg: "))
        altura = float(input("Introducir su altura en metros: "))
        #Calcular el IMC
        imc = peso / (altura ** 2)
        # Determinar la categoría según el IMC   
        if imc < 18.5:
            resultado = "Bajo peso"
        elif imc >= 25:
            resultado = "Sobrepeso"
        else:
            resultado = "Normal"
        # Mostrar el resultado
        print(f"Su índice de masa corporal es: {imc:.2f}. Usted tiene Un Indice IMC {resultado}.")
        #f": Indica que estamos creando una f-string, que es una forma de formatear cadenas en Python. volverlo texto
        #.2f significa que queremos mostrar el valor con dos decimales (es decir, dos dígitos después del punto decimal).
        # Preguntar al usuario si desea calcular otro IMC
        respuesta = input("¿Desea calcular otro IMC? (Sí/No): ").lower()
        if respuesta != 'si':
            break  # Salir del bucle si la respuesta no es 'si'
