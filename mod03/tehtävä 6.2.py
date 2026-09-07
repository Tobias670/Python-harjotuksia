lista=[]
while True:
    numero=(input("Anna luku:\n"))
    if numero=="":
        lista.sort(reverse=True)
        print("Viisi suurinta suuruusjärjestyksessä:")
        print(lista[:5])
        break
    else:
        lista.append(float(numero))