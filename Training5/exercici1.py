# Exercici 1: Funció per calcular el preu total de dos productes

def calcular_preu(preu1, preu2):
    preu1 = int(preu1)
    preu2 = int(preu2)

    result = preu1 + preu2

    return result

resultat = calcular_preu(10, 20)    
print("El preu total és:", resultat)

# 1. Té 2 paràmetres (preu1 i preu2).
# 2. Retorna la suma dels dos preus (la variable result, que en aquest exemple val 30).
# 3. La funció no retornaria res (retornaria None) i el print mostraria: El preu total és: None

# Exercici 2: Funció per aplicar un descompte segons el tipus de client:

def aplicar_descompte(preu, tipus_client):
    tipus = tipus_client.lower()

    if tipus == "particular":
        return preu 
    elif tipus == "empresa":
        return preu * 0.90 
    elif tipus == "client habitual":
        return preu * 0.85 
    else:
        print("Error: El tipus de client no és vàlid.")
        return preu 

print(aplicar_descompte(100, "Particular"))
print(aplicar_descompte(100, "Empresa"))
print(aplicar_descompte(100, "Client habitual"))
print(aplicar_descompte(100, "Desconegut"))

# Exercici 3: Funcions que criden altres funcions

def aplicar_descompte(preu, tipus_client):
    tipus = tipus_client.lower()
    if tipus == "particular":
        return preu
    elif tipus == "empresa":
        return preu * 0.90
    elif tipus == "client habitual":
        return preu * 0.85
    else:
        print("Error: El tipus de client no és vàlid.")
        return preu

def calcular_iva(preu):
    return preu * 0.21

def calcular_factura(preu, tipus_client):
    preu_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descompte)
    return preu_descompte + iva

print(calcular_factura(100, "Particular"))
print(calcular_factura(100, "Empresa"))
print(calcular_factura(100, "Client habitual"))
print(calcular_factura(100, "Altre"))

# Exercici 4: Programa complet: Servei tècnic

def calcular_inicial(peces, obra):
    return peces + obra

def calcular_descompte(preu, tipus):
    if tipus == "vip":
        return preu * 0.10
    return 0

def calcular_iva(preu):
    return preu * 0.21

def calcular_total(preu, iva):
    return preu + iva

def mostrar_menu():
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")
    return input("Selecciona una opció: ")

reparacions = 0
facturacio = 0

opcio = ""
while opcio != "4":
    opcio = mostrar_menu()

    if opcio == "1":
        nom = input("Nom del client: ")
        peces = float(input("Cost peces: "))
        obra = float(input("Cost mà d'obra: "))
        tipus = input("Tipus de client (vip/normal): ")

        inicial = calcular_inicial(peces, obra)
        descompte = calcular_descompte(inicial, tipus)
        subtotal = inicial - descompte
        iva = calcular_iva(subtotal)
        total = calcular_total(subtotal, iva)

        print("\n--- FACTURA ---")
        print("Client:", nom)
        print("Preu inicial:", inicial)
        print("Descompte:", descompte)
        print("IVA:", iva)
        print("Total a pagar:", total)

        reparacions = reparacions + 1
        facturacio = facturacio + total

    elif opcio == "2":
        print("Reparacions realitzades:", reparacions)

    elif opcio == "3":
        print("Facturació acumulada:", facturacio)

    elif opcio == "4":
        print("Adéu!")

# 4. print() només mostra text per pantalla; return envia el resultat al programa per guardar-lo o operar amb ell.
# 5. Perquè el codi queda més ordenat, net i fàcil de corregir.
# 6. És la informació que rep una funció entre parèntesis () per fer la seva feina.
# 7. És una variable creada dins d'una funció que només existeix i es pot fer servir dins d'aquesta.
# 8. Evita repetir codi i permet fer canvis en un sol lloc sense haver de modificar tot el programa.