class TodoList:
    def __init__(self):
        self.todo = {}

    def adauga_task(self,nume, descriere):
        self.nume = nume
        self.descriere = descriere

        self.todo[nume] = descriere

    def afiseaza_todo_list(self):
        print('Task-urile existente: ')
        for i in self.todo.keys():
                print(i)

    def afiseaza_detalii_suplimentare(self, nume_task):



        if nume_task not in self.todo:
           # print("\nTask-ul este in lista")
            raspuns = input ("\nVrei sa adaugi task-ul in lista?: DA sau NU?")
            if raspuns == "DA":
                nume = input("Adauga noul task: ")
                descriere = input("Adauga descrierea noului task")
                todo.adauga_task(nume, descriere)
            else:

                print("La revedere")
        else:
            print(f'\n{self.todo[nume_task]}')
'''
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''




if __name__ == "__main__":
    todo = TodoList()

    todo.adauga_task('Curat', 'Stergere praf in camera')
    todo.adauga_task('Vase', 'Spalare vase ')
    todo.adauga_task('Geamuri', 'Spalare geamuri')

    todo.afiseaza_todo_list()
    nume_task = input("\nCauta un task: ")
    todo.afiseaza_detalii_suplimentare(nume_task)
    todo.afiseaza_todo_list()


