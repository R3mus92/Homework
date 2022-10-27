import sys

sys.path.append(".")

from datetime import date
# from tabulate import tabulate
'''
5.
Clasa Factura
Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie),
numar, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti
Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total
Telefon | 7 | 700 | 49000
'''

class Factura:
    def __init__(self, seria="123451234"):
        self.serie = seria
        self.numar = 2524
        self.nume_produs = "Iphone X"
        self.cantitate = 15
        self.pret_buc = 2000

    def genereaza_factura(self):
        total = self.pret_buc * self.cantitate
        d={
            1: [self.nume_produs,self.cantitate,self.pret_buc,total]

        }
        print(f"\nFactura seria {self.serie} numar {self.numar} ")
        print(f"Generata la data de {date.today()}")
        print("Numar | Produs    | Cantitate | Pret bucata | Total")
        for k , v in d.items():
            self.nume_produs, self.cantitate, self.pret_buc, total = v
            print (k,"    | ", self.nume_produs,"| ", self.cantitate,"      | ",self.pret_buc,"      | ",total)


    def schimba_cantitatea(self,cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self,pret):
        self.pret_buc = pret

    def schimba_nume_produs(self,nume):
        self.nume_produs = nume

    # def genereaza_factura2(self):
    #     total = self.pret_buc * self.cantitate
    #     table = [["1", self.nume_produs, self.cantitate, self.pret_buc, total]]
    #     print(tabulate(table))


if __name__ == "__main__":

    factura = Factura()

    factura.genereaza_factura()
    factura.schimba_cantitatea(20)
    factura.genereaza_factura()
    factura.schimba_pretul(3500)
    factura.genereaza_factura()
    factura.schimba_nume_produs("Samsung A50")
    # factura.genereaza_factura2()

