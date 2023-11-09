class triangulo():#Puede tener hijos
    color="blanco" #atributo de clase mismo valo para todo los objetos de dicha clase
    def __init__(self,base=1, altura=2):#Constructor metodo que se va a ejecutar en el momento es que se cree una estancia se utiliza para inicializar el objeto
        self.base = base #Atributo valor para objeto o instancia
        self.altura= altura #Atributo
    def area(self):#cuando estoy en modelado de objetos debo agragar el slef para que ingrese siempre el parametro debe ser self
        return (self.base*  self.altura)/2
    def pintar(self,nuevo_color):
        color= nuevo_color
        print(f"Este Tirangulo Esta Pintando de color: {color}")

mi_triangulo =  triangulo()
mi_triangulo.base=4 #asignar un valor a mi atributo
mi_triangulo.altura=3
print(f"Área del triángulo: {mi_triangulo.area()}")
mi_triangulo.pintar("rojo")
print(f"Color del triángulo: {mi_triangulo.color}")
class punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y


class Ave():
    def volar(self):
        print("Estoy Volando")
class Caballo():
    def relinchar(self):
        print("Estoy Relicnahdo")
class pegaso(Ave,Caballo):
    def existir(self):
        print("Yo no Existo")   
golondrina=Ave()
golondrina.volar()
rocinante=Caballo()
rocinante.relinchar()
pegasus=pegaso()
pegasus.existir()
pegasus.volar()

