kt="python" 
ss="rules"
count=0
while count !=5:
    arvaus1=input("Anna käyttäjätunnus:\n")
    salis=input("Anna salasana:\n")
    if arvaus1==kt and salis==ss:
        print("Tervetuloa")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana, yritä uudelleen.")
        count+=1
    if count==5:
        print("Pääsy evätty")
        break