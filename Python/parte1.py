'''
#Suma de numeros
#n1=int(input("Ingrese el primer número: "))
#n2 = int(input("Ingrese el segundo número: "))
#n3 = int(input("Ingrese el tercer número: "))
#suma = n1 + n2 + n3
#print(f"La suma entre los valores {n1}, {n2} y {n3} es {suma}")

#Promedio de temperaturas
temp_total=0
dias=["lunes","martes","miercoles","jueves","viernes"]
for elem in dias:
    temp=float(input(f"Ingrese la temperatura del día {elem}: "))
    temp_total=temp_total+temp
promedio=temp_total/len(dias)  
print(f"El promedio de temperatura de los {len(dias)} días es {promedio}")

#Bitcoins a Pesos
btc=float(input("Ingrese la cantidad de BTC que tiene: "))
valor_btc=float(input("Ingresar valor actual del BTC (en pesos): "))
print(f"La cantidad de pesos que equivale sus BTC son: {btc*valor_btc}")

#Descuento en el supermercado
monto_compra=float(input("Ingrese el monto de su compra: "))
if monto_compra>3500:
    desc=monto_compra*0.1
    monto_compra=monto_compra-desc
    print(f"Su monto final a pagar es: {monto_compra} con un descuento de {desc}")

else: 
    print(f"Su monto final a pagar es: {monto_compra} -NO HAY DESCUENTO SEÑORA-")

    #Club deportivo
edad=int(input("Ingrese la edad del asociado: "))
if edad<13:
       print("Eres un pequeñuelo, regresa cuando cumplas al menos 13 crack.")
elif edad<15 and edad>=13:
    print("El asociado pertenece a la categoría infantiles.")
elif edad<17:
        print("El asociado pertenece a la categoría cadetes.")
elif edad<19:
        print("El asociado pertenece a la categoría juveniles.")
else:
        print("El asociado pertenece a la categoría mayores.")
#Asado
carne_persona=0.7
personas=int(input("Franco, ingresá la cantidad de invitados que tienes: "))
precio=float(input("Franco, ingresá el precio de 1 kg de carne: "))
cant_carne=personas*carne_persona
precio_final=precio*cant_carne
print(f"Franco, la cantidad de carne que debes pedir es {cant_carne:.2f} Kg y te costará ${precio_final:.2f}")
       
'''
      

