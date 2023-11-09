mi_otra_tupla = tuple((range(10)))
print(mi_otra_tupla)
otra_tupla=("uno","dos","tres")
print(otra_tupla)
lista=["Carro","Moto","Bicicleta"]
tupla2=tuple(lista)
print(tupla2)
print(tupla2.count("Carro"))#si hay una lista dentro de una tupla, se puede cambiar
tupla3=(8,"Pepito Perez", (2,4,6),[9,8,10])
print(tupla3[-1][::-1])
print(tupla3.index("Pepito Perez"))
print(len(tupla3))
nube=((2.7,3.7),(9,5),(1,5),(3.7,3.2))#Hacer unpacking
for x, y in nube:
    print (f"La Cordenada x es- ",[x], "y la cordenada en Y es ",[y]) 
