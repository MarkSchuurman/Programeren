# Oefening PROG8.1: While-loop & numbers


getal = int(input(f'Geef een getal: '))
aantal_getallen = 0
som = 0

while getal != 0:
    aantal_getallen = aantal_getallen + 1
    som = som + getal
    getal = int(input(f'Geef een getal: '))

print(f'Er zijn {aantal_getallen} ingevoerd, de som is: {som}')
