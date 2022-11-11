from Class_FormaGeometrica import *

patrat = Patrat()
cerc = Cerc()

def test_ariepatrat():
    assert patrat.aria() == 100

def test_ariecerc():
    assert cerc.aria() == 314

def test_descrie():
    assert patrat.descrie() == cerc.descrie()

