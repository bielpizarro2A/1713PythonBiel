numero1=input("Introdueix el primer número: ")
numero2=input("Introdueix el segon número: ")
numero3=input("Introdueix el tercer número: ")

if numero1.isdigit() and numero2.isdigit() and numero3.isdigit():
    numero1 = int(numero1)
    numero2 = int(numero2)
    numero3 = int(numero3)

if numero1 > numero2 and numero1 > numero3:
    print(f"El número més gran és: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El número més gran és: {numero2}")
else:
    print(f"El número més gran és: {numero3}")