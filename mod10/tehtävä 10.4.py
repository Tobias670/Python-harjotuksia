import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusino = self.tämänhetkinen_nopeus+muutos
        if uusino > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif uusino<0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusino

    def kulje(self, aika):
        matka = self.tämänhetkinen_nopeus * aika
        self.kuljettu_matka += matka

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            kiihdytys = random.randint(-10, 15)
            auto.kiihdytä(kiihdytys)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"Kilpailun '{self.nimi}' tilanne")
        for auto in self.autot:
            print(f"Auton rekisteri: {auto.rekisteritunnus} | Huippunopeus: {auto.huippunopeus} km/h | Nykyinen nopeus {auto.tämänhetkinen_nopeus} km/h | Kokonaismatka {auto.kuljettu_matka} km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

autot = []
for item in range(1, 11):
    rekkari = f"ABC-{item}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rekkari, huippu))


romuralli = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    tunnit += 1
  
    if tunnit % 10 == 0:
        print(f"\nAikaa kulunut {tunnit} tuntia.")
        romuralli.tulosta_tilanne()

print(f"\nKilpailu päättyi! Aikaa kului yhteensä {tunnit} tuntia.")
romuralli.tulosta_tilanne()
