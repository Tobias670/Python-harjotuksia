<<<<<<< HEAD
import random
luku= random.randint(1,10)

while True:
    arvaus=int(input("Arvaa luku 1 ja 10 välillä:\n"))
    if arvaus>luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus==luku:
        print("Oikein")
=======
import random
luku= random.randint(1,10)

while True:
    arvaus=int(input("Arvaa luku 1 ja 10 välillä:\n"))
    if arvaus>luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus==luku:
        print("Oikein")
>>>>>>> 3d9d4d2c138a9532f21afd09682d64048319fcfd
        break