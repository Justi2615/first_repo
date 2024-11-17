# program losuje liczbę
# użytkownik zgaduje tę liczbę
# program informuje, czy za dużp, czy za mało, czy ok

import random

liczba = random.randint(0, 100)

while True:
    liczba_uzytkownika = int(input('Podaj liczbę:   '))
    if liczba_uzytkownika == 9999:
        print ('Tryb tajny')
        passwd = input ('Wpisz haslo:   ')
        if passwd == 'Merito':
            break
    elif liczba_uzytkownika > liczba:
        print('Za dużo')
    elif liczba_uzytkownika < liczba:
        print('Za mało')
    else:
        print ('Jest OK')
        break