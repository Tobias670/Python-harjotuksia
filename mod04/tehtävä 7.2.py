import random
def noppa(tahko):
    heitto=random.randint(1,tahko)
    return heitto

tahkol=int(input("Anna nopan maksimisilmäluku:\n"))
while True:
    luku=noppa(tahkol)
    if luku!=tahkol:
        print(f"Heitosta tuli {luku}!")
    elif luku==tahkol:
        print(f"Heitosta tuli {luku}!")
        break
    