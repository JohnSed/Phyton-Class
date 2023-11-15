numero_1 =10
numero_2 = 25
numero_3 = 5
if numero_1 > numero_2 and numero_1 > numero_3:
    print (numero_1)
elif numero_2 > numero_1 and numero_2 > numero_3:
    print (numero_2)
elif numero_3 > numero_1 and numero_3 > numero_2:
    print (numero_3)

class Bus:
    def __init__(self, marca, anio, kilometraje, placa, ruta):
        self.marca = marca
        self.anio = anio
        self.kilometraje = kilometraje
        self.placa = placa
        self.ruta = ruta

    def antiguedad(self):
        if self.anio >= 2022:
            return "nuevo"
        elif self.anio>= 2015 and self.anio <= 2021:
            return "reciente"
        elif self.anio>= 2005 and self.anio <= 2014:
            return "común"
        else:
            return "antiguo"

    def origen(self):
        marcas_europeas = ["Scania", "Volvo", "Daimler", "MAN"]
        if self.marca in marcas_europeas:
            return "europeo"
        else:
            return "otro"
b = Bus("Yutong", 2022, 50000, "DSA963987", "311")
print(b.antiguedad())
print(b.origen())



class Cubo:
    def __init__(self,lado):
        self.lado=lado
    def volumen(self):
        return self.lado**3
    def area(self):
        return 6 * self.lado ** 2
c = Cubo(12)
print(c.volumen())
print(c.area())