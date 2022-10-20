# Oefening PROG8.5: Dict & functions
def namen():
    # maakt de dic aan
    # in een dic is de standaardvolgorde eerst de key en dan de value
    dick = {}
    # loopt door onderstaande heen zo lang het true is (dus bij een input moet er een input zijn)
    while True:
        name = input(str(f'Volgende naam: '))
        # als de naam al in de dic staat dan word er +1 gedaan bij de value
        if name in dick:
            dick[name] += 1
        # als input leeg is wordt de loop gebroken.
        elif name == "" :
            break
        # als de naam nog niet in de dic staat wordt bij de naam value "1" toegekend
        else:
            dick[name] = 1
    # voor iets in de dictionary (!!!!!!!!!!er wordt standaard door de keys geloopt!!!!!!!!!)
    for key in dick:
        # als de value van in dit geval de key groter is dan 1 dan wordt het volgende gedaan:
        if dick[key] > 1:
            # de dick[key] houd in dat de value wordt bekeken en "key" de key zelf
            print(f'Er zijn {dick[key]} studenten met de naam {key} ')
        else:
            print(f'Er is {dick[key]} student met de naam {key}')

namen()

