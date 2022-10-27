# #1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# # Afișeaz-o
# note_muzica = ["do","re","mi","fa","sol","la","si","do"]
# print(note_muzica)
# # Inversează ordinea folosind slicing și suprascrie această listă. Printează varianta actuală (inversată).
# note_muzica = note_muzica[::-1]
# print(note_muzica)
#
# # Pe această listă aplică o metodă care bănuiești că face același lucru,adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
# note_muzica.reverse()
#
# #Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
# print(note_muzica)
#
# #2. De câte ori apare ‘do’?
# print(note_muzica.count("do"))

#3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]. Găsește 2 variante să le unești într-o singură listă
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# # list1.extend(list2)
# # print(list1)
# list3 = list1 + list2
# print(list3)
#
# #4. Sortează și afișează lista generată la exercițiul anterior. Sortează numărul 0 folosind o funcție. Afișaza iar lista.
#
# list3.sort()
# print(list3)
#
# #5. Folosind un if verifică lista generată la exercițiul 3 și afișează:● Lista este goală.● Lista nu este goală.
#
# if len(list3) == 0:
#     print("Lista este goala")
# else:
#     print("Lista nu este goala")
#
# #6. Folosește o funcție care să șteargă lista de la exercițiul 3.
# list3.clear()
# print(list3)
#
# #7. Copy paste la exercițiul 5. Verifică încă o dată. Acum ar trebui să se afișeze că lista e goală.
# if len(list3) == 0:
#     print("Lista este goala")
# else:
#     print("Lista nu este goala")

#8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}. Folosește o funcție că să afișezi Elevii (cheile)

# dict1 = {
#          'Ana' : 8,
#          'Gigel':10,
#          'Dorel':5,
# }
# print(dict1)
# elevii = dict1.keys()
# print(elevii)

#9. Printează cei 3 elevi și notele lor
# x = input("Introdu numele unui elev: ")

# if x == 'Ana':
#     print(dict1.get('Ana'))
# elif x == 'Gigel':
#     print(dict1.get('Gigel'))
# elif x == 'Dorel':
#     print(dict1.get('Dorel'))
# else:
#     print('Elevul nu se afla in lista')

#10. Dorel a făcut contestație și a primit 6.Modifică nota lui Dorel în 6. Printează nota după modificare

# dict1['Dorel'] = 6
# print(dict1.get('Dorel'))

#11. Gigel se transferă din clasă
# dict1.pop('Gigel')
# print(dict1)
# dict1['Ionica'] = 9
#
# print(dict1)

#1. Exerciții Opționale - grad de dificultate: Mediu spre greu (may need Google)


# jucatori_teren = ["Mirel","Dorel","Petre","Vasile","Stefan"]
# print(jucatori_teren)
# schimbari_efectuate = input("Introduce numele schimbarii: ")
# schimbari_max = 3
# jucator = input("Introdu numele jucatorului din teren cu care doresti sa il schimbi: ")
#
# while schimbari_max > 0 and schimbari_max <=3 :
#     if jucator in jucatori_teren:
#         jucatori_teren.remove(jucator)
#         jucatori_teren.append(schimbari_efectuate)
#         schimbari_max = schimbari_max - 1
#         print(f'Jucatorul {schimbari_efectuate} a intrat, jucatorul {jucator} a iesit, mai sunt {schimbari_max} schimbari ')
#         print(jucatori_teren)
#
#     elif schimbari_max == 0:
#         print("Nu mai sunt schimbari disponibile")
#
#     elif jucator not in jucatori_teren:
#         print(f'Nu se poate realiza schimbarea deoarece {jucator} nu este in teren')
#         print(f'Mai ai {schimbari_max} schimbari')
# else:
#     print("Nu mai sunt schimbari disponibile")

# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ
# 1. Adaugă în zilele_sapt ‘luni’. Afișează zile_sapt

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# print(zile_sapt)
# weekend = {'sâmbăta', 'duminică'}
# zile_sapt.add('luni')
# print(zile_sapt)

#2. Folosește un if și verifică dacă:

# if zile_sapt.issubset((weekend)):
#     print('este un subset')
# else:
#     print('nu este un subset')

#3. Afișează diferențele dintre aceste 2 seturi.
# print(zile_sapt.difference(weekend))

#4. Afișează intersecția elementelor din aceste 2 seturi.

# print(zile_sapt.intersection(weekend))


