class Hissi:
    def __init__(self, alink, ylink):
        self.alink = alink
        self.ylink = ylink
        self.nykyinenk = alink

    def kerros_ylös(self):
        if self.nykyinenk < self.ylink:
            self.nykyinenk += 1
            print(f"Hissi on kerroksessa {self.nykyinenk}")

    def kerros_alas(self):
        if self.nykyinenk > self.alink:
            self.nykyinenk -= 1
            print(f"Hissi on kerroksessa {self.nykyinenk}")

    def siirry_kerrokseen(self, kutsuttu):
         if kutsuttu<self.alink or kutsuttu>self.ylink:
              print("Kerrosta ei ole")
              return
         while self.nykyinenk!=kutsuttu:
              if self.nykyinenk<kutsuttu:
                   self.kerros_ylös()
              else:
                   self.kerros_alas()
class Talo:
    def __init__(self,alin,ylin,hissien_määrä):
        self.alin=alin
        self.ylin=ylin

        self.hissit=[]

        for item in range(hissien_määrä):
            uusi_hissi=Hissi(alin,ylin)
            self.hissit.append(uusi_hissi)


    def aja_hissiä(self,hissinnum,kohde_kerros):
        print(f"Hissi numero {hissinnum} on matkalla kerrokseen {kohde_kerros}")
        valittuh=self.hissit[hissinnum-1]
        valittuh.siirry_kerrokseen(kohde_kerros)

talo=Talo(1,5,2)

talo.aja_hissiä(1,5)

talo.aja_hissiä(2,4)
