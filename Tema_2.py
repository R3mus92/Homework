#Exercitiul 1
from random import randint

#un if - else reprezinta o conditie data. Daca aceasta conditie este indeplinita, atunci va rula blocul de cod din interiorul conditiei. Daca conditia nu este indeplinita, va rula blocul de cod existent dupa "else"

#Exercitiul 2

x = 12
if isinstance(x,int) :
    print("Numarul e intreg")
if isinstance(x, float):
    print("Numarul nu e intreg")

#Exercitiul 3

if x <0 :
    print("Numarul este negativ")
elif x==0:
    print("Numarul este neutru")
else:
    print("Numarul este pozitiv")

#Exercitiul 4

x = int(input("Introdu un numar: "))

if -2<x<13:
        print("Numarul este valid")
else:
        print("Numarul este invalid")

#Exercitiul 5

x = int(input("Introduceti primul numar: "))
y = int(input("Introduceti al doilea numar: "))
z = x-y

if (x-y)<5:
    print("Diferenta este mai mica decat 5")
else:
    print("Diferenta este mai mare sau egala decat 5")

#Exercitiul 6

range_1 = range(5, 27, 1)
print (range_1)

x = int(input("Introdu un numar: "))

if x not in range_1 :
    print("Numarul nu este in interval")
else:
    print("Numarul este in interval")

#Exercitiul 7

x = int(input("Introdu x: "))
y = int(input("Introdu y: "))

if x==y:
    print("Numerele sunt egale")
else:
    print("Numarul ce mai mare este: ")
    print(max(x,y))

#Exercitiul 8

x = int(input("Introduceti prima latura: "))
y = int(input("Introduceti a doua latura: "))
z = int(input("Introduceti a treia latura: "))

if x==y==z:
    print("Triunghiul este echilateral")
elif x==y or x==z or y==z:
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")

#Exercitiul 9

litera = input("Introduceti o litera: ")
litera_1 = litera.lower()

if litera_1 == 'a' or litera_1 == 'e' or litera_1 == 'i' or litera_1 == 'o' or litera_1 == 'u':
    print("Litera este o vocala")
else:
    print("Litera nu este o vocala")

#Exercitiul 10

x = int(input("Introduceti o nota: "))

if x>9:
    print("A")
elif x>8:
    print("B")
elif x>7:
    print("C")
elif x>6:
    print("D")
elif x>4:
    print("E")
elif x<=4:
    print("F")


#Exercitiul optional 1
#
x = int(input("Introduceti un numar: "))
y = len(str(x))
print(y)

if y>=4:
    print("Numarul are minim 4 cifre")
else:
    print("Numarul nu are minim 4 cifre")

#Exercitiul optional 2

x = int(input("Introdu un numar: "))
y = len(str(x))

if y==6:
    print("Numarul are exact 6 cifre")
else:
    print("Numarul nu are exact 6 cifre")

#Exercitiul optional 3

x = int(input("Introdu un numar: "))

if x % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")

#Exercitiul optional 4

x = int(input("Introdu primul numar: "))
y = int(input("Introdu al doilea numar: "))
z = int(input("Introdu al treilea numar: "))

print("Cel mai mare numar este: ")
print(max(x,y,z))

#Exercitiul optional 5

x = int(input("Introdu un unghi: "))
y = int(input("Introdu un al doilea unghi: "))
z = int(input("Introdu un al treilea unghi: "))

if x+y+z==180:
    print("Triunghiul este valid")
else:
    print("Triunghiul nu este valid")

#Exercitiul optional 6

prop = "Coral is either the stupidest animal or the smartest rock"

size = len(prop)

x = int(input("Introduceti un numar: "))

mod_string = prop[:size - x]

print(mod_string)


# Exercitiul optional 7

prop = "Coral is either the stupidest animal or the smartest rock"

first = prop[0:5]
last = prop[52:57]

print(first + last)

# Exercitiul optional 8

prop = "Coral is either the stupidest animal or the smartest rock"

index_1 = prop.index("rock")

print(index_1)

size = len(prop)

prop_mod = prop[0:53]
print(prop_mod)


#Exercitiu bonus 11

x = randint(1,6)
y = int(input("Alege un numar de la 1 la 6: "))
print (x)
if y==x:
    print("Felicitari,  ai ghicit!")
elif y<x:
    print("Ai pierdut, numarul a fost mai mic")
else:
    print("Ai pierdut, numarul a fost mai mare")

#Exercitiu studiu in echipa 1

prop = input("Introduceti un string: ")

prop1 = prop.lower()

assert prop1[0] == prop1[-1], 'Primul si ultimul caracter nu sunt la fel.'

print('Primul si ultimul caracter sunt la fel')

#Exercitiu studiu in echipa 2

string = '0123456789'
numere_pare = string[0:9:2]
print(numere_pare)
numere_impare = string[1:10:2]
print(numere_impare)

