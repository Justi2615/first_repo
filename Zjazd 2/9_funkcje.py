slowo = 'Piesek'
liczba = 2.54675675

print(len(slowo))
print(round(liczba, 2))

#def przywitanie():
#    print('Siema')

#przywitanie()

def przywitanie(imie):
    print(f'Siema {imie}')

przywitanie('Kamil')
przywitanie('Monia')

def pole_trojkata(a, h):
    pole = a * h / 2
    return pole

print(pole_trojkata(3,7))

def create_mail(name, age):
    if age < 18:
        print('Nie mozna')
    else:
        if name[-1] == 'a':
            mail = 'Mrs.'+name+'@company.com'

        else:
            mail = 'Mr.'+name+'@company.com'
        return mail

print (create_mail('Kamil', 34))