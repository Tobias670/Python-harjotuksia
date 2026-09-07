import random
noppa=int(input("Kerro noppien määrä\n"))
summa=0
for item in range (noppa):
    heitto=random.randint(1,6)
    print(heitto)
    summa+=heitto
print(f"Silmälukujen summa on {summa}")
