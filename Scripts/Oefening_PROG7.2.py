# Oefening PROG7.2: Lists & numbers
def analyzer():
    lst = "5-9-7-1-7-8-3-2-4-8-7-9"
    gesplitst = lst.split('-')
    number = []
    for getal_als_tekst in gesplitst:
        number.append(int(getal_als_tekst))

    gesorteerde_lijst = number.sort(reverse=True)
    grootste_waarde = max(number)
    kleinste_waarde = min(number)
    aantal_getallen = len(number)
    som_van_de_getallen = sum(number)
    gemiddelde = som_van_de_getallen / aantal_getallen
    return f'Gesorteerde list van ints: {gesorteerde_lijst} \n ' \
           f'Grootste getal: {grootste_waarde} en Kleinste getal: {kleinste_waarde} \n ' \
           f'Aantal getallen: {aantal_getallen} en Som van de getallen: {som_van_de_getallen} \n ' \
           f'Gemiddelde: {gemiddelde} \n'


print(analyzer())
