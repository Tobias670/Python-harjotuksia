vuos=int(input("Syötä vuosiluku\n"))
if(vuos%4==0 and vuos%100!=0) or (vuos%400 ==0):
    print(f"Syöttämäsi vuosiliku {vuos} on karkausvuosi!")
else:
    print(f"Syöttämäsi vuosiliku {vuos} ei on karkausvuosi.")