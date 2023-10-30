empresas={1910:"FORD",1920:"TOYOTA",1930:"BMW",2000:"TESLA" } #Diccionarios Clave:Valor, la calve debe ser inmutable
print(len(empresas))
print(empresas[1930])
print(empresas.get(1920))
empresas[555]=("AUDI")
print(empresas)
print(empresas.keys())#imprimir las claves del diccionario
Estudiantes={1144:("Diaz","Jhon"),182:("Agredo","Sebastian"),788:("Ocoro","Carlos")}#Combinacion de diccionarios y tuplas.
print(len(Estudiantes))#Longitud de el diccionario
Estudiantes[788]=("Lopez", "Johnse")
print(Estudiantes)
print(Estudiantes[1144])#Reetorno de los datos que esten en esta clave
print(Estudiantes.get(788))
Estudiantes[685]=("Agreda","Johan")#Agregar Estudiante Nuevo
print(Estudiantes)
Descalificados = Estudiantes.pop(685) #eliminar un estudiante con la calve dentro de mi diccionario y retorna el valor
print(Descalificados)
del Estudiantes[788] #Elminar data sin retorno ejemplo alt suprimir
print(Estudiantes)
Estudiantes[9501]=("Master","Key")
list(Estudiantes.items()) #convertir mi diccionario en lista en tuplas
list(Estudiantes.keys())# convertir y retornar mi diccionario en una lista mis  claves en tuplas
list(Estudiantes.values())
Cuadrados={x :x**2 for x in range(13) }#Comprehension (Crear un diccionario crear id desde x a y conjunto "Calve - Valor")
print(Cuadrados)
print (6 in Cuadrados )#Me devuelve un valor booleano(false o true si el elemento esta dentro de mi diccionario)
print("25" in Cuadrados)
for clave, valor in Cuadrados.items():
    print(f" {clave} - {valor}")#recorro mi diccionario y toma los valores en x y y