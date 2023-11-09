#Siempre Definimos Una Funcion, siempreen capsulamos nuestra codigo, por orden
def main():
    shopping_lista=[]

    #Ingresaremos un while para llenar nuestra lista
    while True:
        print("\n------Lista De Compras----")#\n guarda la inforamcion en la siguiente linea creando menu a la vista   se imprima un reglon mas abajo
             
        print("1. Agregar Articulo")
        print("2. Eliminar Articulo")
        print("3. Ingrese Valor")
        print("4. Ver Lista")
        print("5. Salir")

        option=input("Por favor Introdusca Una Opcion: ")

        if option == "1":
            item = input ("Introduce Nombre Del Articulo A Agregar: ")
            shopping_lista.append(item) #Va agregando La Informacion A Nuestra Lista Por ORDEN DE INTRODUCCION Como vamos ingresando
        elif option == "2":
            item= input ("Introduce El Producto Que Deseas Elminar: ")
            if item in shopping_lista:
                shopping_lista.remove(item)
            else:
                print("El Articulo No Existe En La Lista") #Da un mensaje de que el articulo no esta dentro de la lista
        elif option == "3":
            valor= int(input("Ingrese El Valor Del Producto: "))
        elif option == "4":
            print ("\n Tu Lista De Compras Es: ")
            for item in shopping_lista:
                print(" - " + item) #Imprime Loque trae mi lista
            if valor in locals():
                print("- Valor : " + str(valor))
        elif option == "5":
            break
        else:
            print ("Opcion Invalida, Verifica La Opcion: ")
if __name__== "__main__":
    main()

