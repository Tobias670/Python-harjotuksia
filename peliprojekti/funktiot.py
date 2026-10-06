import json

tavaraluettelo= []
siirrot=0
kerätyt_lamput=0
arvoesine=0
valmiit_huoneet=[]
parhaat_tulokset={}
Peli=True


def esine(tavaraluettelo):
    tavara = input("Mitä lisätään tavaraluetteloon?\n").lower()
    if len(tavaraluettelo)==1:
        print("Tavararoihisi mahtuu vain yksi tavara, poista ensin aiempi tavara ja sen jälkeen lisää uusi!")
    else:
        print(f"Tavaraluetteloon lisätty {tavara}")
        tavaraluettelo.append(tavara)

def näytä_tavaraluettelo(tavaraluettelo):
    print("Tavaraluettelosi sisältö:")
    for tavara in tavaraluettelo:
        print(tavara)

def poista_tavara(tavaraluettelo):
    tavaraluettelo.clear()

def näytä_tulokset():
    try:
        paras_nimi = min(parhaat_tulokset, key=parhaat_tulokset.get)
        paras_siirrot = parhaat_tulokset[paras_nimi]
        print("Paras tulos:")
        print(f"1. {paras_nimi}: {paras_siirrot} siirtoa")
    
    except ValueError:
        print("Tulostaulu on vielä tyhjillään, kokeile pelata peli!")

def aloitapeli():
    import pelikoodi
    pelikoodi.aloitapeli()

def tallenna_tilanne(nimi,sijainti,tavaraluettelo,siirrot,kerätyt_lamput,arvoesine,valmiit_huoneet,parhaat_tulokset):
        tallennus_data = {
        "pelaaja": nimi,
        "tavaraluettelo": tavaraluettelo,
        "sijainti":sijainti,
        "siirrot": siirrot,
        "kerätyt_lamput": kerätyt_lamput,
        "arvoesine": arvoesine,
        "valmiit_huoneet": valmiit_huoneet,
        "parhaat_tulokset":parhaat_tulokset,
}
        global Peli
        with open("tallennus.json","w") as tiedosto:
            json.dump(tallennus_data,tiedosto)
        print("Peli tallennettu")
        Peli=False

def lataa_tilanne(nimi):
    import ast  # Tarvitaan listan ja sanakirjan (dict) turvalliseen lukemiseen tekstistä

def lataa_tilanne(nimi):
    try:
        with open("tallennus.json", "r", encoding="utf-8") as tiedosto:
            return json.load(tiedosto)
    except FileNotFoundError:
        return None