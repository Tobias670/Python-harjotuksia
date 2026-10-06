import paavalikko
import funktiot
import random

class Pelaaja:
    def __init__(self, nimi, tavara,sijainti="eteinen"):
        self.nimi=paavalikko.nimi
        self.tavara=funktiot.tavaraluettelo
        self.sijainti=sijainti

    def siirry_huoneeseen(self):
        tarkistus=0
        while tarkistus!=1:
            liike=input("Mihin huoneeseen haluat mennä?\n\nKirjoita haluamasi huone, kuten eteinen, makuuhuone, keittiö, olohuone, kylpyhuone, kellari.\nTai haluatko tallentaa pelin, tällöin kirjoita 'tallenna':\n").lower()
            if liike=='tallenna':
                funktiot.tallenna_tilanne(self.nimi,self.sijainti,self.tavara,funktiot.siirrot,funktiot.kerätyt_lamput,funktiot.arvoesine,
                                          funktiot.valmiit_huoneet,funktiot.parhaat_tulokset)
                tarkistus+=1
                
            sattuma=random.randint(1,20)
            if "otsalamppu" not in self.tavara and sattuma==1:
                print("Kävellessäsi toiseen huoneeseen et huomaa mattoa\n\nyksi keräämistäsi hehkulampuistasi meni repussasi rikki" )
                funktiot.kerätyt_lamput-=1

            if liike=="keittiö":
                print("Menit keittiöön\n")
                self.sijainti=liike
                funktiot.siirrot+=1
                tarkistus+=1
                
            elif liike=="olohuone":
                print("Menit olohuoneeseen\n")
                self.sijainti=liike
                funktiot.siirrot+=1
                tarkistus+=1

            elif liike=="kylpyhuone":
                print("Menit kylpyhuoneeseen\n")
                self.sijainti=liike
                funktiot.siirrot+=1
                tarkistus+=1

            elif liike=="kellari":
                print("Astut kellariin\n")
                self.sijainti=liike
                funktiot.siirrot+=1
                tarkistus+=1

            elif liike=="eteinen":
                print("Menit eteiseen\n")
                self.sijainti=liike
                funktiot.siirrot+=1
                tarkistus+=1

            elif liike=="makuuhuone":
                print("Menit makuuhuoneeseen\n")
                self.sijainti=liike
                funktiot.siirrot+=1
                tarkistus+=1
            else:
                print("Huomio! Syötä jokin olemassa olevan huoneen nimi!")
            
        tapahtuma=random.randint(1,15)
        if tapahtuma==1:
            print("Liikkuessasi talossa näet jotain kimmeltävää silmäkulmassasi.\nLöysit arvoesineen!")
            funktiot.arvoesine+=1

    def vaihda_lamppu(self):
         if self.sijainti in funktiot.valmiit_huoneet:
            print(f"Huomio! Olet jo vaihtanut '{self.sijainti}' lamput!")
            return
         vaihto=input("Haluatko vaihtaa huoneen molemmat lamput? vastaa kirjoittamalla 'kyllä' tai 'ei':\n").lower()

         if vaihto=="ei":
              print("Päätit olla vaihtamatta huoneen lamppuja")
            
         elif vaihto==("kyllä"):
            print("Ryhdyit hommiin ja alat vaihtamaan huoneen lammpuja")
                 
            varovaisuus=random.randint(1,25)
            if varovaisuus==1 and "jakkara" not in self.tavara:
                 print("Kurottelet kattoon varpaillasi ja lamppu lipsahtaa käsistäsi ja tippuu lattielle menien rikki")
                 funktiot.kerätyt_lamput-=1
            else:
                 print(f"Hetken ajan jälkeen sait kaikki lamput vaihdettua huoneesta{self.sijainti}")
                 funktiot.siirrot+=1
                 funktiot.kerätyt_lamput+=2
            funktiot.valmiit_huoneet.append(self.sijainti)

class Huone:
        def __init__(self,nimi="eteinen",lamput=2):
             self.nimi=nimi
             self.lamput=lamput

class Vaihdetut_lamput:
     def __init__(self,nimi,määrä,arvo=2):
          self.nimi=nimi
          self.arvo=arvo
          self.määrä=määrä

eteinen=Huone("Eteinen")
makuuhuone=Huone("Makuuhuone")
keittiö=Huone("Keittiö")
olohuone=Huone("Olohuone")
kylpyhuone=Huone("Kylpyhuone")
kellari=Huone("Kellari")