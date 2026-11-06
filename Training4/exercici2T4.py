hi_ha_deu = False

numero = float(input("Introdueix una nota (de 0 a 10, o -1 per acabar): "))
while numero != -1:
    if numero == 10:
        hi_ha_deu = True
    numero = float(input("Introdueix una nota (de 0 a 10, o -1 per acabar): "))

if hi_ha_deu:
    print("Hi ha al menys una nota de 10.")
else:
    print("No hi ha cap nota de 10.")