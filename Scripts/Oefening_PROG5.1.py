# Oefening PROG5.1: Functie met drie parameters
# maakt de functie "som() aan"
def som():
    # makt de variabelen aan voor in de functie
    getal1 = int(input("Voer hier een cijfer in: "))
    getal2 = int(input("Voer hier een cijfer in: "))
    getal3 = int(input("Voer hier een cijfer in: "))
    # telt de variabelen bij elkaar op
    uitkomst = getal1 + getal2 + getal3
    # de output is uitkomst
    return uitkomst


# print de functie om de variabele uitkomst te krijgen
print(som())
