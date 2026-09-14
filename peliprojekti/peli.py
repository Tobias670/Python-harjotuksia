tavaraluettelo= []
vtaso= "Normaali"

def esine(tavaraluettelo):
    tavara = input("Mitä lisätään tavaraluetteloon?\n")
    tavaraluettelo.append(tavara)

def näytä_tavaraluettelo(tavaraluettelo):
    print("Tavaraluettelosi sisältö:")
    for tavara in tavaraluettelo:
        print(tavara)

def vaihda_vaikeustaso():
    print("Valitse haluamasi vaikeustaso:")
    print("Helppo - valitse 1")
    print("Normaali - valitse 2")
    print("Vaikea - valitse 3")
    global vtaso
    vtaso = input("Syötä valitsemasi taso numerolla:\n")
    if vtaso == "1":
        print("Vaikeustaso vaihdettu vaikeudelle: Helppo")
        vtaso = "Helppo"
    elif vtaso == "2":
        print("Vaikeustaso vaihdettu vaikeudelle: Normaali")
        vtaso = "Normaali"
    elif vtaso == "3":
        print("Vaikeustaso vaihdettu vaikeudelle: Vaikea")
        vtaso = "Vaikea"

def aloitapeli():
    print(f"Peli alkaa vaikeustasolla {vtaso}...")

nimi= input("Mikä on nimesi\n")
ikä= int(input("Mikä on ikäsi\n"))
lk=0
while lk<1:
    if ikä<12:
        print("Olet alaikäinen")
        break
    else:
        print(f"Moi {nimi}!")
        lk+= 1
    while True:
        print("Päävalikko")
        print("Aloita peli 1.")
        print("Avaa tavaraluettelo 2.")
        print("Vaihda vaikeustasoa 3.")
        print("Lopeta peli 4.")
        valitse = input("Valitse komentoa vastaava numero tai kirjoita 'lopeta'\n")
        
        if valitse == "1":
            aloitapeli()
        elif valitse == "2":
            valinta = input("Syötä 1, jos haluat nähdä tavaraluettelon ja numero 2, jos haluat lisätä tavaraluetteloon tavaroita:\n")
            if valinta == "1":
                näytä_tavaraluettelo(tavaraluettelo)
            elif valinta == "2":
                esine(tavaraluettelo)
        elif valitse == "3":
            vaihda_vaikeustaso()
        elif valitse == "4" or valitse == "lopeta":
            print("Peli sammuu")
            break
