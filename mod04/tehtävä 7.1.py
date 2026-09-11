import random
def noppa():
    heitto=random.randint(1,6)
    return heitto

while True:
    luku=noppa()
    if luku!=6:
        print(f"Heitosta tuli {luku}!")
    elif luku==6:
        print(f"Heitosta tuli {luku}!")
        break
    