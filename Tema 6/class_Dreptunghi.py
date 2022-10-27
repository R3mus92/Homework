'''2.
Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param
o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin
apelarea metodei descrie()
'''

class Dreptunghi:
    def __init__(self,lungime_p,latime_p,culoare_p):
        self.lungime = lungime_p
        self.latime  = latime_p
        self.culoare = culoare_p

    def descrie_dreptunghi(self):
        print(f'\n Lungimea dreptunghiului este {self.lungime}, latime dreptunghiului este {self.latime} si culoarea dreptunghiului este {self.culoare} ')

    def aria(self):

        return self.lungime * self.latime

    def perimetrul(self):

        return 2*self.latime + 2*self.latime

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare



if __name__ == "__main__":
    lungime_introdusa = int(input("Introdu lungimea: "))
    latime_introdusa = int(input("Introdu latimea: "))
    culoare_introdusa = input("Introdu culoare: ")


    dreptunghi = Dreptunghi(lungime_introdusa,latime_introdusa,culoare_introdusa)

    dreptunghi.descrie_dreptunghi()

    print(f'\n Aria dreptunghiului este: {dreptunghi.aria()}')
    print(f'\n Perimetrul dreptunghiului este: {dreptunghi.perimetrul()}')

    dreptunghi.schimba_culoarea("Albastru")
    dreptunghi.descrie_dreptunghi()

