def main():
    shopping_lista = []

    while True:
        print("\n------Lista De Compras----")
        print("1. Agregar Articulo")
        print("2. Eliminar Articulo")
        print("3. Ingrese Valor")
        print("4. Ver Lista")
        print("5. Salir")

        option = input("Por favor Introduzca Una Opción: ")

        if option == "1":
            item = input("Introduce Nombre Del Articulo A Agregar: ")
            shopping_lista.append({"item": item, "valor": None})
        elif option == "2":
            item = input("Introduce El Producto Que Deseas Eliminar: ")
            item_found = False
            for product in shopping_lista:
                if product["item"] == item:
                    shopping_lista.remove(product)
                    item_found = True
                    break
            if not item_found:
                print("El Articulo No Existe En La Lista")
        elif option == "3":
            valor = int(input("Ingrese El Valor Del Producto: "))
            item = input("Introduce Nombre Del Articulo: ")
            for product in shopping_lista:
                if product["item"] == item:
                    product["valor"] = valor
                    break
        elif option == "4":
            print("\nTu Lista De Compras Es:")
            for product in shopping_lista:
                print(" - Ítem:", product["item"])
                print("   Valor:", product["valor"])
        elif option == "5":
            break
        else:
            print("Opción Inválida, Verifica La Opción")

if __name__ == "__main__":
    main()
