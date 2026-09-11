import math
def laske(halkaisija, hinta):
    säde = (halkaisija / 2) / 100
    pinta_ala = math.pi * (säde ** 2)
    yksikköh = hinta/pinta_ala
    return yksikköh

d1=float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä:\n"))
hinta1=float(input("Anna ensimmäisen pizzan hinta euroina:\n"))

d2=float(input("Anna toisen pizzan halkaisija senttimetreinä:\n"))
hinta2= float(input("Anna toisen pizzan hinta euroina:\n"))

hinta1 = laske(d1, hinta1)
hinta2 = laske(d2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta: {hinta1:.2f} €/m^2")
print(f"Toisen pizzan yksikköhinta: {hinta2:.2f} €/m^2")

if hinta1 < hinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahallesi!")
elif hinta2 < hinta1:
    print("Toinen pizza antaa paremman vastineen rahallesi!")
else:
    print("Pizzat maksaa saman verran")