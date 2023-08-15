print("Hola. A continuación seleccione una de las opciones disponibles: ")

VALOR1="NULL"
VALOR2="NULL"

while opcion!=7: 

    print("/n")
    print(f"1. Ingresar valor 1 ({VALOR1})")
    print(f"2. Ingresar valor 2 ({VALOR2})")
    print("3. Mostrar suma")
    print("4. Mostrar resta")
    print("5. Mostrar multiplicación")
    print("6. Mostrar división")
    print("7. Salir")
    print("/n")
    
    opcion=int(input("Elija una opción:"))
    print("/n")

    if opcion==1:
        VALOR1=int(input("Ingresar el valor 1: "))
    if opcion==2:
        VALOR2=int(input("Ingresar el valor 2: "))
    print("/n")

    if VALOR1=="NULL":
        print("Falta ingresar el valor 1")

    elif VALOR2=="NULL":
        print("Falta ingresar el valor 2")
    
    else:
        if opcion==3:
            print(F"El valor de la suma es: {VALOR1+VALOR2}")
        if opcion==4:
            print(F"El valor de la resta es: {VALOR1-VALOR2}")
        if opcion==5:
            print(F"El valor de la multiplicacion es: {VALOR1*VALOR2}")
        if opcion==6:
            print(F"El valor de la division es: {VALOR1/VALOR2}")



