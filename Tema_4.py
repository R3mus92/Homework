# 1. Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# '''    a) Folositi un for ca sa iterati prin toata lista si sa afisati
#           ‘Masina mea preferata este x’
#        b) Faceti acelasi lucru cu un for each
#        c) Faceti acelasi lucru cu un while
# '''
# for i in range (len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
# for elem in masini:
#     print(f'Masina mea preferata este {elem}')

# ind = 0
# while ind<(len(masini)):
#     print(f'Masina mea preferata este {masini[ind]}')
#     ind+=1

#2. Aceeasi lista. Folositi un for. In for, modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei

# for i in masini[1:len(masini)-1]:
#     print(i.upper())

#3.
'''
Aceeasi lista,
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
Printam ‘am gasit masina dorita de dvs’
Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
Printam Am gasit masina X. Mai cautam
'''
# for i in masini:
#     if i == 'Mercedes':
#         print("Am gasit masina dorita de dvs, Mercedes")
#         break
#     else:
#         print(f'Am gasit masina {i} , mai cautam')

#4
'''
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si
Lastun.
Daca masina e Trabant sau Lastun
Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
'''

# for i in masini:
#     if i == 'Trabant' or i == 'Lastun':
#         continue
#     else:
#         print(f'S-ar putea sa va placa masina {i}')


#5
'''
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
- Salvati aceste masini in masini_vechi
- Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''
# masini_vechi = []
#
# for i in range(len(masini)):
#     if masini[i] == 'Trabant' or masini[i] == 'Lastun':
#
#         masini_vechi.append(masini[i])
#         print(masini_vechi)
#         masini[5] = 'Tesla'
#         masini[7] = 'Tesla'
#         print(masini)
#


#6. Avand dict

# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }

# Vine un client cu un buget de 15000 euro.
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

# for i in pret_masini:
#     if pret_masini.get(i) > 15000:
#         print(i)
#
# y = pret_masini.items()
# print(y)
# print(type(y))
# for i in y:
#         if i[1]<15000:
#            print(f'Pentru un buget de sub 15000 de euro puteti alege masina {i[0]}')
#

#7.
'''
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea. Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# count = 0
# for i in numere :
#     if i == 3 :
#         count = count + 1
# print(count)
#8.
'''
Aceeasi lista. Iterati prin ea. Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# sum = 0
# for i in range (0 , len(numere)):
#     sum  = sum + numere[i]
# print(sum)

#9.
'''
Aceeasi lista. Iterati prin ea. Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# max = numere[0]
#
# for num in numere:
#     if num > max:
#         max = num
# print(max)

#10.
'''
Aceeasi lista. Iterati prin ea. Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# for elem in range (len(numere)):
#     if numere[elem] > 0:
#         numere[elem] = numere[elem] * (-1)
# print(numere)


###### Optionale (may need google) #####

# 11.
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere
Populati corect celelalte liste
Afisati cele 4 liste la final
'''

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for i in range(len(alte_numere)):
#     if alte_numere[i] % 2 == 0:
#         numere_pare.append(alte_numere[i])
#     elif alte_numere[i] % 2 != 0:
#         numere_impare.append(alte_numere[i])
#
#     if alte_numere[i] > 0:
#         numere_pozitive.append(alte_numere[i])
#     elif alte_numere[i] < 0:
#         numere_negative.append(alte_numere[i])
#
# print(f'Numerele pare sunt: {numere_pare}')
# print(f'Numerele impare sunt: {numere_impare}')
# print(f'Numerele pozitive sunt: {numere_pozitive}')
# print(f'Numerele negative sunt: {numere_negative}')

# 12.
'''
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici : https://www.youtube.com/watch?v=lyZQPjUT5B4 
'''


alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for i in range(len(alte_numere)):

     for j in range(0,(len(alte_numere)-i-1)):

        if alte_numere[j] > alte_numere[j+1] :
           alte_numere[j],alte_numere[j + 1] = alte_numere[j + 1],alte_numere[j]

print(alte_numere)

