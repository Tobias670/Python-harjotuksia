class Julkaisu:
    def __init__(self,nimi):
        self.nimi=nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja=kirjoittaja
        self.sivumäärä=sivumäärä
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumäärä}")
class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja=päätoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}, Päätoimittaja: {self.päätoimittaja}")
lehti=Lehti("Aku Ankka","Aki Hyyppä")
kirja=Kirja("Hytti n:o 6","Rosa Liksom","200 sivua")

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()