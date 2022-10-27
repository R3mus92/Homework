''' 1.
Clasa Cerc
Atribute: raza, culoare
Constructor pt ambele atribute
Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''


class Cerc:

    def __init__(self, raza_p, culoare_p):
        self.raza = raza_p
        self.culoare = culoare_p

    def descrie_cerc(self):
        print(f'\n Raza cercului este {self.raza} si culoarea cercului este {self.culoare}')

    def aria(self):
        return 3.14 * self.raza * self.raza

    def diametru(self):
        return self.raza+self.raza

    def circumferinta(self):
        return 3.14 * (self.raza+self.raza)



if __name__ == "__main__":
    raza_introdusa = int(input("Introdu raza: "))
    culoare_introdusa = input("Introdu culoare: ")
    cerc = Cerc(raza_introdusa, culoare_introdusa)

    cerc.descrie_cerc()
    print(f'\n Aria cercului este: {cerc.aria()}')
    print(f'\n Diametrul cercului este: {cerc.diametru()}')
    print(f'\n Circumferinta cercului este: {cerc.circumferinta()}')

