for i in range (20+1):
    if i%3 ==0 :
        continue# se salta las demas funciones del if y regresa al siguiente line del for
    print(i)
while True: #Ciclo Infinito, con expresion bulanea al ser booleana
    nombre= input("Ingrese Un Nombre")
    if nombre =="Eladio":
        continue
    print(nombre)
    print("Fin")
#Con este se vuelve infinito

    while True: #Ciclo Infinito, con expresion bulanea al ser booleana
        nom= input("Ingrese Un Nombre")
        if nom =="Eladio":
            print("Ok")
        else:
            break
    print(nom)