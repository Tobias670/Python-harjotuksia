import funktiot

nimi= input("Mikä on nimesi?\n")

ikä= int(input("Mikä on ikäsi?\n"))
lk=0

while lk<1:
    if ikä<12:
        print("Olet alaikäinen")
        break
    else:
        print(f"Moi {nimi}!")
        lk+= 1
with open(r"c:\Users\User\Desktop\Python harjotuksia\peliprojekti\intro.txt","r", encoding="utf-8") as f:
              ohje=f.read()
              print(ohje)
while True:
    print("\nPäävalikko")
    print("Aloita peli 1.")
    print("Avaa tavaraluettelo 2.")
    print("Näytä pelin paras tulos 3.")
    print("Näytä pelin ohjeet 4.")
    print("Jatka peliä 5")
    print("Lopeta peli 6.")
    valitse = input("Valitse komentoa vastaava numero tai kirjoita 'lopeta'\n")
        
    if valitse == "1":
        funktiot.aloitapeli()
            
    elif valitse == "2":
            print("\nHuomaa, että voit ottaa mukaan vain yhden tavaran mukaan, joista hyötyjä antaa:\njakkara, otsalamppu")
            valinta = input("\nSyötä 1, jos haluat nähdä tavaraluettelon. \nSyötä 2, jos haluat lisätä tavaraluetteloon tavaran.\nSyötä 3, jos haluat poistaa tavaran tavaraluettelosta:\n")
            if valinta == "1":
                funktiot.näytä_tavaraluettelo(funktiot.tavaraluettelo)
            elif valinta == "2":
                funktiot.esine(funktiot.tavaraluettelo)
            elif valinta =="3":
                funktiot.poista_tavara(funktiot.tavaraluettelo)
    elif valitse == "3":
            funktiot.näytä_tulokset()
    elif valitse =="4":
         with open(r"c:\Users\User\Desktop\Python harjotuksia\peliprojekti\ohjeet.txt","r", encoding="utf-8") as f:
              ohje=f.read()
              print(ohje)
    elif valitse == "5":
          nimi=input("Syötä tallennusta vastaava nimi:\n")
          ladatut_tiedot=funktiot.lataa_tilanne(nimi)
          if ladatut_tiedot is not None:
            import pelikoodi
            pelikoodi.aloitapeli(*ladatut_tiedot) 
          else:
                ("Tallennusta ei löytynyt...")
        
    elif valitse == "6" or valitse == "lopeta":
            print("Peli sammuu")
            break
