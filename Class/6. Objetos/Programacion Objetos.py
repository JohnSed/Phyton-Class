class triangulo():#Puede tener hijos
    color="blanco" #tributo de clase mismo valo para todo los objetos de dicha clase
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
print()
class punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __add__(self, otro_punto):#Para usar formulas matematicas debo primero agregarlo en mi def de objeto
        return punto(self.x + otro_punto.x,self.y +otro_punto.y)
    def __str__(self) -> str:
        return f"X= {self.x}, Y= {self.y}" 
P1=punto(5,6)
PS=punto(7,-2)
Nuevo_punto=P1+PS
print(Nuevo_punto.x)
print(Nuevo_punto.y)
print(Nuevo_punto)
print()
class Televisor():
    def __init__(self, canal_actual=3, volumen_Ac=10,color="negro"):
        self.canal_actual=canal_actual
        self.volumen_Ac=volumen_Ac
        self.color=color
    def mute(self):
        self.volumen_Ac=0
class SmartTv(Televisor):
    def __init__(self, canal_actual=3, volumen_Ac=10,color="negro", Wifi= False ):
        super().__init__(canal_actual,volumen_Ac,color)
        self.Wifi=Wifi
    def chek_wf (self):
        if self.Wifi== True:
            return("Wify Activado")  
        else:
            return("Wifi Desactivado") 
Mi_Tv=Televisor()
Mi_Tv.canal_actual=1
Mi_Tv.volumen_Ac=20
Mi_Tv.mute()
mi_smartv= SmartTv(8,11,"Gris")
print(mi_smartv.canal_actual)
 


print()       
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

