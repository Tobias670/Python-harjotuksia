Leiviskä=(float)(input("Anna leivisköjen määrä\n"))
Naula=(float)(input("Anna naulojen määrä\n"))
Luoti=(float)(input("Anna luotien määrä\n"))
Lepaino = (Leiviskä*20*32*13.3)
Napaino = (Naula*32*13.3)
Lupaino = (Luoti*13.3)
Yhtpaino=(Lepaino+Napaino+Lupaino)
kg=Yhtpaino//1000
gramma=Yhtpaino%1000
print(f"Massa nykymitoissa\n{kg:.0f} kilogrammaa ja {gramma:.2f} grammaa")