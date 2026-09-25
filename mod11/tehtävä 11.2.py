class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.tämänhetkinen_nopeus=0
        self.kuljettu_matka=0
    def kiihdytä(self,muutos):
        uusino=self.tämänhetkinen_nopeus+muutos
        if uusino>self.huippunopeus:
            self.tämänhetkinen_nopeus=self.huippunopeus
        elif uusino<0:
            self.tämänhetkinen_nopeus=0
        else:
            self.tämänhetkinen_nopeus=uusino
    def kulje(self,aika):
        matka=self.tämänhetkinen_nopeus*aika
        self.kuljettu_matka=self.kuljettu_matka+matka
class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,akkukapasiteetti):
        self.akkukapasiteetti=akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus,bensatankki):
        self.bensatankki=bensatankki
        super().__init__(rekisteritunnus, huippunopeus)    

uusi=Auto("ABC-123",142)

sähköauto1=Sähköauto("ABC-15",180,"52,5kWh")
polttomoottoriauto1=Polttomoottoriauto("ACD-123",165,"32,3 l")

sähköauto1.kiihdytä(80)
polttomoottoriauto1.kiihdytä(100)

sähköauto1.kulje(3)
polttomoottoriauto1.kulje(3)

print(f"Sähköautolla kuljettu matka: {sähköauto1.kuljettu_matka} km")
print(f"Sähköautolla kuljettu matka: {polttomoottoriauto1.kuljettu_matka} km")