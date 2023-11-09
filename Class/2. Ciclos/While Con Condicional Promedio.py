grades=[] # Un arreglo vacio ya que tomara todo los numeros a ingresar mi diferente nombre
while True: #Identacion
        grade= input("Ingrese Calificacion O salir para Terminar: ")
        if grade.lower()=="salir": #Vuelva lo que ingrese en minuscula
            break #Termina El codigo
        else:
              grades.append(float(grade))# Llena en ultima pocision, crea un menu donde guarda la informacion "Lista" Float numero decimal, el floar vuelve mi variable en decimal
avarage = sum(grades)/len(grades) #len crea longitud (cantidad ) de datos
print("El Promedio De Notas es ", avarage)

