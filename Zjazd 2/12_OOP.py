class Auto:
    def __init__(self):
        self.kolor = 'black'                                # dzięki self możemy używać parametrów w każdej funkcji
        self.ilosc_paliwa = 10
        self.kondycja = 5
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.mandaty = []
        self.komentarze = []

Audi438 = Auto()
BMW12 = Auto()

Audi438.kondycja = 4
print(Audi438.kolor)
print(Audi438.kondycja)


class Auto:
    def __init__(self, barwa: str, paliwo: int, wiek: int):
        self.kolor = barwa
        self.ilosc_paliwa = paliwo
        self.kondycja = 5
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.mandaty = []
        self.komentarze = []
        self.rocznik = 2024 - wiek

    def __str__(self):
        return (f'Rocznik:{self.rocznik}, mandaty: {self.mandaty}')

Audi438 = Auto('red', 5,23)
BMW12 = Auto('blue', 2, 1)

def zasieg(self):
    zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100
    return  round(zasieg * 0.9)

def ustaw_tryb(self, tryb):
    if tryb == 'eco':
        self.spalanie_na_100 = 10
        self.tryb_ekonomiczny = 