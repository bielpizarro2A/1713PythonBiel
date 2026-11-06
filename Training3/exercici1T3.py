edat=input("Introdueix la teva edat: ")

if edat.isdigit():
    edat = int(edat)
    if edat < 18:
        print("Ets menor d'edat.")
    else:
        print("Ets major d'edat.")