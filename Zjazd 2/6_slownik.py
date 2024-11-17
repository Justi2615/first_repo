zakupy = ['chleb', 'mleko', 'platki', 'platki']
uzytkownicy = ['Kamil', 'Python123', 'Monia', 'Monia1', 'Monia']
hasla =       ['123',   'asfaf3f',   'Piesek', '1234',  'dsdf']

users = {
    'Kamil': '123',
    'Python': 'asfaf3f',
    'Monia': 'Piesek',
    'Monia1': '1234'
}

print (users)
#print (users[2])                           Tak nie można, bo pary nie mają numerów
print (users['Kamil'])                      #Wypisujemy hasło dla Kamila
users['Mariusz'] = '4356'                   #Dodajemy usera i hasło dla niego
users['Monia'] = 'Kotek'                    #Zmieniamy hasło, bo Monia istnieje

