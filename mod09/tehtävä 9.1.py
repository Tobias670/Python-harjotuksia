class Auto:
    def __init__(self,rekisteritunnus, huippunopeus):
        self.rekisteritunnus=rekisteritunnus
        self.huippunopeus=huippunopeus
        self.tämänhetkinen_nopeus=0
        self.kuljettu_matka=0

uusi=Auto("ABC-123",142)
print(f"Rekisteritunnus: {uusi.rekisteritunnus}")
print(f"Huippunopeus: {uusi.huippunopeus}")
print(f"Tämänhetkinen nopeus: {uusi.tämänhetkinen_nopeus}")
print(f"Kuljettu matka {uusi.kuljettu_matka}")