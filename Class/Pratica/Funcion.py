def OperadorMat (Operador,Valor1,Valor2):
    if Operador=="-":
        return Valor1-Valor2
    if Operador=="+":
        return Valor1+Valor2
    if Operador=="*":
        return Valor1*Valor2
    if Operador=="/":
        if Valor2==0:
            print("Error: Divisor incorrecto")
            return None  # Para manejar el caso de división por cero
    return Valor1/Valor2
Operador=input("Ingrese Operador(Suma, Division. Multiplicacion, Resta): ")
Operador=Operador.lower()#Volver en minuscula
Valor1=float(input("Ingrese Numero 1: "))
Valor2=float(input("Ingrese Numero 2: "))
if Operador in ("suma","+"):
    Operador="+"
elif Operador in ("resta","-"):
    Operador="-"
elif Operador in ("division","/"):
    Operador="/"
elif Operador in ("multiplicacion","*"):
    Operador="*"
else:
    print("Operador no reconocido. Por favor, ingrese uno válido (suma, resta, división o multiplicación).")
resultado=OperadorMat(Operador,Valor1,Valor2)#Debo asignar en una variable lo que se debe asignar

if resultado is not None:
    print(f"Resultado: {Valor1} {Operador} {Valor2} = {resultado}")
