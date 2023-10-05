# Siempre definimos una función y siempre encapsulamos nuestro código, por orden
def main():
    shopping_lista = []

    # Ingresaremos un while para llenar nuestra lista
    while True:
        print("\n------Lista De Compras----")  # \n guarda la información en la siguiente línea creando un menú a la vista
        print("1. Agregar Articulo")
        print("2. Eliminar Articulo")
        print("3. Ver Lista")
        print("4. Salir")

        option = input("Por favor, introduzca una opción: ")

        if option == "1":
            item = input("Introduce Nombre Del Articulo A Agregar: ")
            shopping_lista.append(item)  # Va agregando la información a nuestra lista por orden de introducción como vamos ingresando
        elif option == "2":
            item = input("Introduce El Producto Que Deseas Eliminar: ")
            if item in shopping_lista:
                shopping_lista.remove(item)  # Elimina el elemento de la lista
            else:
                print("El artículo no está en la lista.")
        elif option == "3":
            print("\nTu Lista De Compras Es:")
            for item in shopping_lista:
                print(" - " + item)
        elif option == "4":
            break
        else:
            print("Opción Invalida. Verifica la opción.")

if __name__ == "__main__":
    main()