def summalista(lista1):
    summa=0
    for luku1 in lista1:
        summa+=luku1
    return summa

luvut=[8, 12, 4]
summat=summalista(luvut)
print(f'Listan lukujen summa on {summat}')