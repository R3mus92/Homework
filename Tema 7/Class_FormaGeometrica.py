from abc import ABC, abstractmethod


class FormaGeometrica(ABC):

    def __init__(self):
        self.PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        pass

class Patrat(FormaGeometrica):
    def __init__(self):
        super().__init__()
        self.__latura = 10

    def get_latura(self):
        return self.__latura

    def set_latura(self):
        self.__latura = 5
        return self.__latura

    def delete_latura(self):
        self.__latura = 0
        return self.__latura

    def descrie(self):
        print("Cel mai probabil am colturi")

    def aria(self):
        return self.__latura * self.__latura


class Cerc(FormaGeometrica):
    def __init__(self):
        super().__init__()
        self.__raza = 10

    def get_raza(self):
        return self.__raza

    def set_raza(self):
        self.__raza = 5
        return self.__raza

    def delete_raza(self):
        self.__raza = 0
        return self.__raza

    def aria(self):
        return self.PI * self.__raza * self.__raza

    def descrie(self):
        print("Cel mai probabil nu am colturi")


if __name__=="__main__":

    patrat = Patrat()
    patrat.descrie()

    print(f"Aria patratului 1 este: {patrat.aria()}")
    patrat.set_latura()
    print(f"Aria patratului 2 este: {patrat.aria()}")
    patrat.delete_latura()
    print(f"Aria patratului 3 este: {patrat.aria()}")


    cerc = Cerc()
    cerc.descrie()

    print(f"Aria cercului 1 este : {cerc.aria()}")
    cerc.set_raza()
    print(f"Aria cercului 2 este : {cerc.aria()}")
    cerc.delete_raza()
    print(f"Aria cercului 3 este : {cerc.aria()}")
