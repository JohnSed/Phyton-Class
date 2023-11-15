# Data analisis 
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Imprime el la última fila de year y pop

print (year[-1])
print (pop[-1])

# Importa matplotlib.pyplot como plt
import matplotlib.pyplot as plt

# Haz un gráfico de líneas: año en el eje x, pop en el eje y
plt.plot(year, pop)

# Muestra el gráfico con plt.show()
plt.show()

#Historigrama
valores=[0,1,2,2,3,3,4,4,5,6,7,8,2]
print(valores.count)
