def litra(gallo):
    muunnos=(gallo*3.785)
    return muunnos

while True:
    gallot=float(input("Anna galloonamäärä tai syötä negatiivinen luku lopettaaksesi:\n"))
    määrä=litra(gallot)
    if määrä>0:
        print(f"{gallot} galloonaa on {määrä:.2f} litraa")
    elif määrä <0:
        break