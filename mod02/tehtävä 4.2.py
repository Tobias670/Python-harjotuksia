hytti=(str)(input("Onko hyttisi LUX, A, B vai C? Syötä hyttiluokka isoin kirjaimin.\n"))
if hytti == "LUX": # type: ignore
    print("LUX on parvekkeellinen hytti yläkannella")
elif hytti =="A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif hytti =="B":
    print("B on ikkunanaton hytti autokannen yläpuolella")
elif hytti =="C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print('Virheellinen hyttiluokka')