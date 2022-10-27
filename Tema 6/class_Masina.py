class Masina:
    def __init__(self,model,viteza_maxima):
        self.model = model
        self.viteza_max = viteza_maxima
        self.culoare = "gri"
        self.viteza_actuala = 0
        self.culori_disponibile = {"alb", "albastru", "verde"," negru","mov"}
        self.marca = "Audi"
        self.inmatriculata = False


    def descrie(self):
        print(f'\n {self.marca} modelul {self.model} are culoarea {self.culoare}, viteza maxima este de {self.viteza_max}, este sau nu inmatriculata: {self.inmatriculata}, in momentul acesta are viteza {self.viteza_actuala}')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
              self.culoare = culoare
              masina.descrie()
        else:
              print(f"\n Culoarea {culoare} nu se afla in lista de optiuni")

    def accelereaza(self,viteza):
        for i in range(viteza):
            if viteza < 0:
                print("Eroare, viteza e negativa")
            elif viteza <= self.viteza_max:
                self.viteza_actuala = viteza
                print(f"Viteza actuala a masinii este: {i+1}")
            elif viteza > self.viteza_max:
                self.viteza_actuala = self.viteza_max
                print(self.viteza_max)
                break

    def franeaza(self):
        self.viteza_actuala = 0
        return self.viteza_actuala


if __name__ == "__main__":
    masina = Masina("A6 c7",290)

    masina.descrie()
    culoare = input("\n Alege o culoare: ")
    masina.vopseste(culoare)
    viteza_masinii = int(input("Introdu viteza masinii: "))
    masina.accelereaza(viteza_masinii)
    print(f"Viteza masinii este {masina.franeaza()}, masina a franat")

