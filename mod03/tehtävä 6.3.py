<<<<<<< HEAD
luku=int(input("Anna kokonaisluku\n"))

alkuluku= True

if luku<=1:
    alkuluku=False
else:
    for item in range(2,luku):
        if luku % item==0:
            alkuluku=False
            break
if alkuluku:
    print(f'Luku {luku} on alkuluku')
else:
=======
luku=int(input("Anna kokonaisluku\n"))

alkuluku= True

if luku<=1:
    alkuluku=False
else:
    for item in range(2,luku):
        if luku % item==0:
            alkuluku=False
            break
if alkuluku:
    print(f'Luku {luku} on alkuluku')
else:
>>>>>>> 3d9d4d2c138a9532f21afd09682d64048319fcfd
    print(f"Luku {luku} ei ole alkuluku")