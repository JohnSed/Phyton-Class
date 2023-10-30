#Volver dos listas en un solo diccionario
lista_1=[30, 20, 10,0]
lista_2=['Madrid', 'París', 'Berlín',"Barcola"]
if len(lista_1)==len(lista_2):#Verifico que las listas tengan el mismo tamaño longitudinal
    mi_diccionario={}
    for i in range(len(lista_1)):
        mi_diccionario[lista_1[i]]=lista_2[i]#.
        print(mi_diccionario)
    for clave, pais in mi_diccionario.items():
        print(f"{clave} - {pais}")

else:
    print("La Listas No Tienen El Mismo tamño de longitud")
#Unir Tuplas y cambiar su orden
tupla_1=('C', 'C++', 'Rust')
tupla_2=('Java', 'Scala', 'Kotlin')
tupla_1, tupla_2 = tupla_2[::-1], tupla_1[::-1] #orden diferente y que itenere desde el ultimo hacia rriba
print(f"{tupla_1}{tupla_2}")
#____________________
lista=['Noruega', 'Suecia', 'Dinamarca']
diccionario={'Suiza': 7.26, 'Uruguay': 6.85, 'Noruega': 6.59, 'Suecia': 5.62, 'Dinamarca': 5.41, 'Argentina': 5.31, 'Zona euro': 5.29, 'Estados Unidos': 5.15}
nuevo_diccionario={i:diccionario[i] for i in lista if i in diccionario}#.
print(nuevo_diccionario)
#______
tupla=('Alemania', 'Alemania', 'Francia')
verif=all(i==tupla[0] for i in tupla)
print(verif)

