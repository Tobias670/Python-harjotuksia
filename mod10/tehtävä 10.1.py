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

h = Hissi(1, 5)

print("Hissin ovet sulkeutuu ja hissi lähtee ylöspäin")
h.siirry_kerrokseen(5)

print("Hissin ovet sulkeutuu ja hissi lähtee alaspäin")
h.siirry_kerrokseen(1)             