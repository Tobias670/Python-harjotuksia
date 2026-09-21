import random
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

autot=[]

for item in range(1,11):
    rekkari=(f"ABC-{item}")
    huippu=random.randint(100,200)

    uusi_auto=Auto(rekkari,huippu)
    autot.append(uusi_auto)

kilpailu=True

while kilpailu:
    for auto in autot:
        kiihdytys=random.randint(-10,15)
        auto.kiihdytä(kiihdytys)

        auto.kulje(1)

        if auto.kuljettu_matka>=10000:
            kilpailu=False

for auto in autot:
    print (f"{auto.rekisteritunnus} |Huippunopeus: {auto.huippunopeus}km/h | Nykyinen nopeus: {auto.tämänhetkinen_nopeus}km/h | Kokonaismatka: {auto.kuljettu_matka}km")

uusi=Auto("ABC-123",142)
