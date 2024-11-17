do_kupienia = ['marchew', 'chleb', 'masło', 'mleko']
w_domu = ['miod', 'chleb', 'mleko', 'pomidor', 'sok']

for produkt in do_kupienia:
    if produkt in w_domu:
        print (produkt)

# program napisze co kupic

for produkt in do_kupienia:
    mam = False
    for item in w_domu:
        if produkt == item:
            mam = True
            print(f'Nie kupuj {produkt}')
    if mam == False:
        print (f'Kup {produkt}')

print('Drugie podejscie')

for produkt in do_kupienia:
    if produkt not in w_domu:
        print(f'Kup {produkt}')


