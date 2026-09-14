def f(parittomatp):
    l2=[]
    for luku in l1:
        if luku%2==0:
            l2.append(luku)
    return l2

l1=[1,2,3,4,5,6,7,8,9,10]
parittomatp=f(l1)

print(f"Alkuperäinen lista: {l1}")
print(f'Parillisten lukujen lista {parittomatp}')