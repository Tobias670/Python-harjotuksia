sukup= input("Mikä on biologinen sukupuolesi?\n")
hemog= float(input("Anna hemoglobiinisi arvo muodossa g/l\n"))
if sukup=="mies":
    if hemog<=134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemog >=195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print ("Hemoglobiiniarvo on normaali.")
elif sukup=="nainen":
    if hemog<=117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemog >=175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print ("Hemoglobiiniarvo on normaali.")