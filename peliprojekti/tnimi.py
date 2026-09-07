<<<<<<< HEAD
nimi= (str)(input("Mikä on nimesi\n"))
ikä= (int)(input("Mikä on ikäsi\n"))
lk=0
while lk<1:
    if ikä<12:
        print("Olet alaikäinen")
        break
    else:
        print(f"Moi {nimi}!")
        lk+=1
while True:
    print("Päävalikko")
    print("Aloita peli 1.")
    print("Lue pelin ohjeet 2.")
    print("Parhaat pisteet 3.")
    print("Lopeta peli 4.")
    valitse=(input("Valitse komentoa vastaava numero tai kirjoia 'lopeta'\n"))
    if valitse=="1":
        print("Peli alkaa...")
    elif valitse=="2":
        print("Tässä on ohjeet peliin:")
    elif valitse=="3":
        print("Tässä ovat 5 parasta tulosta:")
    elif valitse=="4" or valitse=="lopeta":
        print("Peli sammuu")
=======
nimi= (str)(input("Mikä on nimesi\n"))
ikä= (int)(input("Mikä on ikäsi\n"))
lk=0
while lk<1:
    if ikä<12:
        print("Olet alaikäinen")
        break
    else:
        print(f"Moi {nimi}!")
        lk+=1
while True:
    print("Päävalikko")
    print("Aloita peli 1.")
    print("Lue pelin ohjeet 2.")
    print("Parhaat pisteet 3.")
    print("Lopeta peli 4.")
    valitse=(input("Valitse komentoa vastaava numero tai kirjoia 'lopeta'\n"))
    if valitse=="1":
        print("Peli alkaa...")
    elif valitse=="2":
        print("Tässä on ohjeet peliin:")
    elif valitse=="3":
        print("Tässä ovat 5 parasta tulosta:")
    elif valitse=="4" or valitse=="lopeta":
        print("Peli sammuu")
>>>>>>> 3d9d4d2c138a9532f21afd09682d64048319fcfd
        break