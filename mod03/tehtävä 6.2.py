<<<<<<< HEAD
lista=[]
while True:
    numero=(input("Anna luku:\n"))
    if numero=="":
        lista.sort(reverse=True)
        print("Viisi suurinta suuruusjärjestyksessä:")
        print(lista[:5])
        break
    else:
=======
lista=[]
while True:
    numero=(input("Anna luku:\n"))
    if numero=="":
        lista.sort(reverse=True)
        print("Viisi suurinta suuruusjärjestyksessä:")
        print(lista[:5])
        break
    else:
>>>>>>> 3d9d4d2c138a9532f21afd09682d64048319fcfd
        lista.append(float(numero))