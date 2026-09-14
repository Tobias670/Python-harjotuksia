
luvut=[]
while True:
    sluku=(input("Syötä luku:\n"))
    if sluku=="":
        print("Pienin:",min(luvut))
        print("Suurin:",max(luvut))
        break
    luku= float(sluku)
    luvut.append(luku)