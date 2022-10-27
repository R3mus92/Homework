'''
4.
Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate
Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)
'''

class Cont:
    def __init__(self):
         self.iban = "RO29PORL2375265893773475"
         self.titular_cont = "Mircea Ion"
         self.sold = 2500

    def afisare_sold(self):
        print(f'\n Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self,suma):
        self.sold = self.sold - suma

    def creditare_cont(self,suma):
        self.sold = self.sold + suma


if __name__ == "__main__":
    cont_pers = Cont()

    cont_pers.afisare_sold()

    suma_1 = int(input("\n Alege suma de retragere din cont: "))

    cont_pers.debitare_cont(suma_1)

    cont_pers.afisare_sold()

    suma_2 = int(input("\n Alege suma de creditare in cont: "))

    cont_pers.creditare_cont(suma_2)

    cont_pers.afisare_sold()
