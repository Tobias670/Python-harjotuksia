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

    

uusi=Auto("ABC-123",142)
uusi.kiihdytä(30)
uusi.kiihdytä(70)
uusi.kiihdytä(50)

print(f"Auton nopeus nyt: {uusi.tämänhetkinen_nopeus}km/h")

uusi.kiihdytä(-200)
print(f"Auton nopeus hätäjarrutukse jälkeen: {uusi.tämänhetkinen_nopeus}km/h")

print(f"Rekisteritunnus: {uusi.rekisteritunnus}")
print(f"Huippunopeus: {uusi.huippunopeus}")
print(f"Tämänhetkinen nopeus: {uusi.tämänhetkinen_nopeus}")
print(f"Kuljettu matka {uusi.kuljettu_matka}")