import unittest

from Class_FormaGeometrica import *

patrat = Patrat()
cerc = Cerc()

#1. Alegeti 3 functii din cele implementate la tema anterior, si scrieti unit tests pentru ele folosind unittest

class ExampleUnittests(unittest.TestCase):
    def test_arie_patrat(self):
        self.assertEqual(patrat.aria(), 100)


    def test_arie_cerc(self):
        self.assertEqual(cerc.aria(), 314)

    def test_descrie(self):
        self.assertEqual(patrat.descrie(),cerc.descrie())

#2. Alegeti 2 clase din cele implementate la tema anterior, si scrieti unit teste pentru toate metodele folosind unittest.

    def test_clasa_patrat(self):
        self.assertEqual(patrat.get_latura(), 10)
        self.assertEqual(patrat.set_latura(), 5)
        self.assertEqual(patrat.delete_latura(), 0)

    def test_clasa_cerc(self):
        self.assertEqual(cerc.get_raza(), 10)
        self.assertEqual(cerc.set_raza(), 5)
        self.assertEqual(cerc.delete_raza(), 0)

if __name__ == "__main__":
    unittest.main()
