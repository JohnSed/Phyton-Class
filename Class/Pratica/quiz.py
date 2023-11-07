base:2
altura:1
def area_triangulo(base,altura):
    return (base*altura/2)

def es_impar(numero):
    if numero % 2 == 0:
        return False
    else:
        return True 
          
num=es_impar(-2)
print(num)

def es_primo(numero):
    if numero % 2 == 0:
        return False
    else:
        return True 
          
num=es_impar(-2)
print(num)
def es_primo(numero):
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    if numero % 2!= 0:
        return False
print(es_primo(5)) 
nume=input("Ingrese Numero A:")
num2=input("Ingrese Numero B:")
nume
def Multi():
    global nume
    global num2
    return float(nume)*float(num2)

Multi()