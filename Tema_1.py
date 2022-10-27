# Exercitiul 1
# #o variabila se poate asocia cu un container cu un nume pentru un anumit set de biti sau tip de date

# Exercitiul 2
text1 = "Masina"
numar = 44
numar_float = 2.55
sunt_acasa = True

# Exercitiul 3
print('Exercitiul 3')
print(type(text1))
print(type(numar))
print(type(numar_float))
print(type(sunt_acasa))

# Exercitiul 4
print('Exercitiul 4')
numar_float=round(numar_float)
print(type(numar_float))


######################################################


#Exercitiul 5
print('Exercitiul 5')
print(f'Aceasta este o : {text1}')
print(f'Un numar aleator: {numar}')
print(f'Numarul ales este: {numar_float}')
print(f'Eu sunt acasa acum: {sunt_acasa}')

######################################################


#Exercitiul 6
print('Exercitiul 6')
read_1 = input('Inroduceti numele: ')
read_2 = input('Inroduceti prenumele: ')
print(f'Numele tau complet este: {read_1} {read_2}')

######################################################


#Exercitiul 7
print('Exercitiul 7')
lungimea = int(input('Introduceti lungimea dreptunghiului: '))
latimea = int(input('Introduceti latimea dreptunghiului: '))
x = lungimea * latimea
print(f'Aria dreptunghiului este: {x}')

######################################################


#Exercitiul 8/9
print('Exercitiul 8/9')
just_string = 'Coral is either the stupidest animal or the smartest rock'
x = (just_string.count(' the'))
print(f'Cuvantul "the" apare de: {x} ori')

######################################################


#Exercitiul 10


print('Exercitiul 10')
contains_digit = False
just_string = 'Coral is either the stupidest animal or the smartest r0ck'
for character in just_string:
    if character.isdigit():
        contains_digit = True

print(contains_digit)

######################################################


# Exercitiul optional 1
text = input('Introdu o propozitie: ')

text_length = len(text)

print(f'Propozitia are {text_length} caractere')

def middle_char (txt):
    return txt[(len(txt)-1)//2:(len(txt)+2)//2]

if (text_length%2)==0:
    print ('Introdu alt text de dimensiune impara')
else:
    print('Caracterul din mijloc al propozitiei este:',middle_char(text))


######################################################


# Exercitiul optional 2
just_string = input('Introduceti o propozitie: ')
text = just_string.split()
print(text)

mydict = {}

for index in range(len(text)):
    mydict["var_%d" %index] = text[index]
    print('var_%d: '%index+text[index])


