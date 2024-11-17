#x = 0
#while x < 5:
#    print('Wykonuje kod')                    Nie zmieniamy x, więc będzie się printować w nieskończoność

x = 0
while x <5:
    print('Wykonuje kod')
    x += 1                                      #Dodaj do x 1
print('koniec')

passwd = '1234'
user_passwd = input('Podaj hasło:   ')
while user_passwd != passwd:
    user_passwd = input('Podaj hasło:   ')
print('hasło poprawne')