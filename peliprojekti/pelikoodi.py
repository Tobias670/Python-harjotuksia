import funktiot
import paavalikko
def aloitapeli(nimi=None, sijainti="eteinen", tavara=None, siirrot=0, kerätyt_lamput=0, arvoesine="0", valmiit_huoneet=None, parhaat_tulokset=None):
    import luokat
    
    if tavara is None:
        tavara = []
    if valmiit_huoneet is None:
        valmiit_huoneet = []
    if parhaat_tulokset is None:
        parhaat_tulokset = {}

    print(f"Peli alkaa...")

    funktiot.tavaraluettelo = tavara
    funktiot.siirrot = siirrot
    funktiot.kerätyt_lamput = kerätyt_lamput
    funktiot.arvoesine = arvoesine
    funktiot.valmiit_huoneet = valmiit_huoneet
    funktiot.parhaat_tulokset = parhaat_tulokset
    funktiot.Peli = True 

    pelaaja = luokat.Pelaaja(nimi=nimi, sijainti=sijainti,tavara=funktiot.tavaraluettelo)

    print(f"Mukanasi on {funktiot.tavaraluettelo} ja astut sisään vanhaan taloon\n")

    while funktiot.Peli == True:
        print(f"Pelaaja on huoneessa {pelaaja.sijainti}")
        print(f"Pelaajan löytämien arvoesineiden määrä: {funktiot.arvoesine}\n")
        print(f"Pelaajan vaihtamien ja kerättyjen hehkulamppujen määrä: {funktiot.kerätyt_lamput}")

        pelaaja.siirry_huoneeseen()

        if funktiot.Peli == False:
            break

        pelaaja.vaihda_lamppu()
        
        if funktiot.kerätyt_lamput >= 10 or funktiot.arvoesine == 4 or (funktiot.kerätyt_lamput >= 5 and funktiot.arvoesine == 2):
            print(f"Voitit pelin!\n\nPelaaja {pelaaja.nimi} voitti pelin {funktiot.siirrot}:n siirron aikana")
            funktiot.parhaat_tulokset[pelaaja.nimi] = funktiot.siirrot
            break

    print("Palataan päävalikkoon...")