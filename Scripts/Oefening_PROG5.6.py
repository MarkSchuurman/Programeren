# Schrijf (en test) de functie wijzig() met één parameter: letterlijst.
# Zorg dat de functie de lijst leegt en de letters [ ‘d’, ‘e’, ‘f’ ] toevoegt.
# Er is geen return-waarde! Test je programma als volgt:

def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')


# of:

def wijzig(letterlijst):
    for letter in list(letterlijst):  # maar als je hier die list() vergeet gebeuren er rare dingen!
        letterlijst.remove(letter)
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')


lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

# dus ik kan je aanraden om te kijken waarom deze versie niet werkt:
# def wijzig(letterlijst):
#     for letter in letterlijst:
#         letterlijst.remove(letter)
#     letterlijst.append('d')
#     letterlijst.append('e')
#     letterlijst.append('f')
