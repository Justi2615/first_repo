NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2          część wspólna
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

print(f'\nChorzy w ostatnim roku na krzykach: {chorzy_rok & krzyki}')
print(f'ilość: {len(krzyki & chorzy_rok)}')

print(f'\nChorzy w ostatnim miesiącu na krzykach: {chorzy_miesiac & krzyki}')
print(f'ilość: {len(krzyki & chorzy_miesiac)}')

print(f'\nChorzy w ostatnim miesiącu w centrum: {chorzy_miesiac & centrum}')
print(f'ilość: {len(centrum & chorzy_miesiac)}')

print(f'\nOsoby w centrum i na krzykach: {krzyki | centrum}')
print(f'ilość: {len(krzyki | centrum)}')

# sprawdźmy poprawność danych:
print('Poprawność danych')

# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku

print(f'\nLiczba ludzi, którzy chorowali w ostatnim miesiącu, ale nie w roku: ({chorzy_miesiac} - {chorzy_rok})')
print(f'\Ilość {len(chorzy_miesiac - chorzy_rok)}')
if len(chorzy_miesiac - chorzy_rok) == 0:
    print('ok')

# nikt nie powinien mieszkać jednocześnie w centrum i na krzykach, jeśli tak, trzeba usunąć
duplikaty = krzyki & centrum
if len(duplikaty) != 0:
    print('\nznaleziono duplikaty - usuwam')
    krzyki = krzyki - duplikaty
if len(krzyki & centrum) == 0:
    print('ok, brak duplikatów')

# kaźdy: chory, zdrowy, z krzyków i z centrum powinien być w bazie NFZ. Jeśli nie ma, trzeba dopisać
# pesele żeńskie mają ostatnią cyfrę parzystą, męskie - nieparzystą
# wypiszmy mężczyzn z centrum, którzy nie byli chorzy w ostatnim roku