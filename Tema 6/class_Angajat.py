'''
3.
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent
'''

class Angajat:
    def __init__(self):
        self.nume = input("Introdu un nume: ")
        self.prenume = input("Introdu un prenume: ")
        self.salariu = int(input("Introdu salariul: "))

    def descrie(self):
        print(f'\n Numele si prenumele salariatului este {self.nume} {self.prenume} si salariul acestuia este de {self.salariu} lei')

    def nume_complet(self):
        print(f'\n Numele complet al salariatului este: {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'\n Salariul lunar al lui {self.prenume} este de {self.salariu} lei ')

    def salariu_anual(self):
        print(f'\n Salariul anual al lui {self.prenume} este de {self.salariu * 12} lei ')

    def marire_salariu(self,procent):
        procentul_marit = self.salariu * (procent/100)
        self.salariu = procentul_marit + self.salariu




if __name__ == "__main__":
    angajat_1 = Angajat()
    angajat_1.descrie()
    angajat_1.nume_complet()
    angajat_1.salariu_lunar()
    angajat_1.salariu_anual()
    procentul_ales = int(input("\n Introdu cu ce procent se mareste salariul: "))
    angajat_1.marire_salariu(procentul_ales)
    angajat_1.salariu_lunar()
    angajat_1.salariu_anual()
    