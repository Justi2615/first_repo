# Stwórz bazę użytkowników (imię, nazwisko, wiek)
# Baza to lista, użytkownik to słownik

emp1 = {'imie': 'Anna', 'nazwisko': 'Kowalska', 'wiek': 18}
emp2 = {'imie': 'Karol', 'nazwisko': 'Nowak', 'wiek': 15}

user_database = [emp1, emp2]

print(user_database[1]['nazwisko'])

wiek_suma = 0
sredni_wiek = 0
for user in user_database:
    user['mail'] = user['imie']+'.'+ user['nazwisko'] + '@merito.pl'
    wiek_suma += user['wiek']
sredni_wiek = wiek_suma/len(user_database)
print(f'sredni wiek {sredni_wiek}')
print(user_database)