Cajon=[5000,"factura", "reloj", 10000,"audifonos"]#Programacion De Listas - Mutables o modificables.
print(Cajon)
Cajon.append(["peine",500])#Agregar elementos a la lista se ordenan como el ultimo, Y SE AGREGA COMO UNA NUEVA LISTA DENTRO DE LA LISTA "anidadas"
print(Cajon)
Cajon.append(["cargador"])
print(Cajon)
Cajon[5]="recibo de luz"#modificar dentro de la lista general la poscion 5 la nueva informacio
print(Cajon)
Cajon.insert(4,["cepillo", "colgate", 200])#Insertar elemento con la pocision que deseo o antes del indice que deseo
print(Cajon)
print(Cajon[0])#Ingresar el imprimir solo un indice expecifico de mi lista, de acuerdo a su posicion
print(Cajon[6])
print(Cajon[4][1])# Como acceder al elemnto dentro de la lista anidada
print(Cajon[-1])#Imprimir elemento de atras a adelante
print(Cajon[len(Cajon)//2])#acceder a la mitad de la inforamcion de uan lista grande
otro_cajon=["Desodorante","Gafas","Gorra"]
nochero=Cajon+otro_cajon#Concatenar elementos
print(nochero)
nochero.pop(5)#Eliminar
print(nochero)
#Slicing permite acceder aun conjunto de elementos de la lista
print(nochero[4:6])
#Repetir Una Lista
nochero2=nochero[4:6] * 3
print(nochero2)
#Membership buscar si un elemento hace parte de la lista
print("reloj" in nochero) #da una respuesta de falso
nuevo=nochero2[:3]
print(nuevo)
print(id(nuevo))
print(Cajon.index(5000))
nochero2.extend([200,300,400])#coloca cada elemento por separado por una lista
print(nochero2)
print(nuevo)
print(nochero2)
#nochero2.sort()#ordenar ascendente solo tipos compatibles
print(len(nochero2))
#Comprehension
# Se desea crear una lista de conjunto de numero que cumplan cierta parte que desee secuenci de numeros o similar
numeros=[1,2,3,4,5,6]
numero2= [i for i in range(1,10+1,2)]
print(numero2)
lista = [i for i in range(1, 101) if i % 3 == 0]
print(lista)