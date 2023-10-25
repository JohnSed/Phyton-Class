lista=[2,7,6,5]
suma_impares = 0
multiplicacion_pares = 1


for numero in lista:
    if numero % 2 == 0: 
        multiplicacion_pares *= numero
    else:  
        suma_impares += numero

print("Suma de los números impares:", suma_impares)
print("Multiplicación de los números pares:", multiplicacion_pares)