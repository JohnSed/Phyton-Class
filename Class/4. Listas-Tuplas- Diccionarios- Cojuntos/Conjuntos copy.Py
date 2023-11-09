mi_conjunto={2,7,9,3,1}#en los conjuntos los datos ingresados no se ordenan. esto impiden que por index podamos ingresar, elementos no ordenados

print(mi_conjunto)
mi_conjunto.add("hermano")#agregar elementos al conjunto
print(mi_conjunto)
lista=[1,2,3,4]
miotroconjunt=set(lista)
print(miotroconjunt)
miotroconjunt.update((-1,-5,-8,-4))#agregar varios elementos
print(miotroconjunt)
miotroconjunt.discard((-1,-5,-8,-4)) # eliminar un elemento de mi conjunto, no se repite en los conjutos
print(miotroconjunt)
miotroconjunt.remove(-1)
print(miotroconjunt)
miotroconjunt.pop()
print(miotroconjunt)
#operaciones
A={1,2,3,4,5,6,7}
B={9,8,7,6,5,4,3}
B.union(A)
print(B)
A|B 
A.intersection(B)
print(A)
A&B
print(A)
A.symmetric_difference(B)
print(A)
B.difference(A)
print(B)#loque no esta en el conjunto a y si en el b
empresas={1910:"FORD",1920:"TOYOTA",1930:"BMW",2000:"TESLA" } #Diccionarios Clave:Valor
print(len(empresas))
print(empresas[1930])
print(empresas.get(1920))
empresas[555]=("AUDI")
print(empresas)
empresas.keys()#imprimir las claves del diccionario
