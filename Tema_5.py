# 1. Functie care sa calculeze si sa returneze suma a 2 numere

def suma (a,b):

    rez = a+b
    return rez


# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def even_odd():
    number = int(input("Enter number : "))
    if number % 2 == 0:
        return True
    else:
        return False


#3. Functie care returneaza numarul total de caractere din numele tau complet. (nume, prenume, nume_mijlociu)
def total_caractere():
    name = input("Enter your name: ")
    name2 = name.replace(" ","")

    return len(name2)


#4. Functie care returneaza aria dreptunghiului
def aria_dreptunghiului():
    latimea = int(input("Introduceti latimea: "))
    lungimea = int(input("Introduceti lungumea: "))
    return lungimea * latimea


#5. Functie care returneaza aria cercului
def aria_cercului():
    raza = int(input("Introduceti raza cercului: "))
    return 3.14 * raza*raza

#6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
def string_caract():
    str = input("Introdu un string: ")
    caract = input("Introdu un caracter: ")
    print(f'Caracterul "{caract}" se afla in string?: ')
    return (caract in str)

'''7. Functie fara return, primeste un string si printeaza pe ecran:
- Nr de caractere lower case este x
- Nr de caractere upper case este y
'''
def lower_upper():
    string = input("Introdu un string: ")
    lower = []
    upper = []
    for i in range(len(string)):
        if string[i].islower():
            lower.append(string[i])
        elif string[i].isupper():
            upper.append(string[i])
    print(lower)
    print(upper)
    print(len(lower))
    print(len(upper))

#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def positive(lista):
    for elem in range(len(lista)):
        if lista[elem] < 0:
            lista[elem] = lista[elem] * -1
    return lista

'''
9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
- Primul numar x este mai mare decat al doilea nr y
- Al doilea nr y este mai mare decat primul nr x
- Numerele sunt egale.
'''
def compare():
    x = int(input("Introdu primul numar x: "))
    y = int(input("Introdu al doilea numar y: "))
    if x>y:
        print("Primul numar x este mai mare decat al doilea numar y ")
    elif x<y:
        print("Al doilea numar y este mai mare decat primul x")
    else:
        print("Numere sunt egale")

'''
10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
'''
def set_numar():
    set_input = input("Enter a set: ")
    convert_set = set(set_input.strip().split())
    print(convert_set)
    number = input("Enter a number: ")
    if number in convert_set:
        print("Nu am adaugat numarul in set. Acesta exista deja: ", False)
    else:
        convert_set.add(number)
        print ("Am adaugat numarul in set: ", True)
        print(convert_set)

###  Optionale (may need google) ###

#11. Functie care primeste o luna din an si returneaza cate zile are acea luna
def luna_an():
    luna = input("Introdu o luna: ")
    luna.lower()
    if luna == 'ianuarie':
        print('31')
    elif luna == 'februarie':
        print('28')
    elif luna == 'martie':
        print('31')
    elif luna == 'aprilie':
        print('30')
    elif luna == 'mai':
        print('31')
    elif luna == 'iunie':
        print('30')
    elif luna == 'iulie':
        print('31')
    elif luna == 'august':
        print('31')
    elif luna == 'septembrie':
        print('30')
    elif luna == 'octombrie':
        print('31')
    elif luna == 'noiembrie':
        print('30')
    elif luna == 'decembrie':
        print('31')
    else:
        print("Nu exista acea luna")





if __name__ == "__main__":

# Exercitiul 1

    # x = int(input("Introdu primul numar: "))
    # y = int(input("Introdu al doilea numar: "))
    #
    # result1 = suma(x,y)
    # result2 = suma(10,20)
    #
    # print(result1)
    # print(result2)

# Exercitiul 2
#     print(even_odd())

# Exercitiul 3
#     print (f'Numarul total de caractere din nume este: {total_caractere()}')

# Exercitiul 4
#     print(f'Aria dreptunghiului este: {aria_dreptunghiului()}')

# Exercitiul 5
#     print(f'Aria cercului este: {aria_cercului()}')

# Exercitiul 6
#     print(string_caract())

# Exercitiul 7
#     lower_upper()

# Exercitiul 8
#     a = list(map(int,input("Introdu numerele din lista: ").strip().split()))
#     print(positive(a))

# Exercitiul 9
#     compare()

# Exercitiul 10
#     set_numar()

### . Optionale (may need google) ###

# Exercitiul 11
    luna_an()
