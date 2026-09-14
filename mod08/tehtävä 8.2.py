lista=set()
uusi=input("Syötä nimi:\n")
while True:
    if uusi=="":
        for item in (lista):
            print (item)
        break
    elif uusi not in lista:
        print("Uusi nimi")
        lista.add(uusi)
    else:
        print("Aiemmin syötetty nimi")
    uusi=input("Syötä nimi:\n")

