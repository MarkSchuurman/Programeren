# Oefening PROG9.1: Sets

bruin = {'Boxtel', 'Best', 'Eindhoven', 'Helmond t Houd', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}


def overeenkomst():
    print(f'de overeemkomende stations zijn: {bruin.intersection(groen)}')


overeenkomst()


def verschillen():
    print(f'de volgende stations heeft Bruin WEL en Groen NIET: {bruin.difference(groen)}')
    print(f'de volgende stations heeft Groen WEL en Bruin NIET: {groen.difference(bruin)}')


verschillen()


def totaal():
    print(f'samen hebben deze 2 trajecten de volgende stations: {groen.union(bruin)}')


totaal()
