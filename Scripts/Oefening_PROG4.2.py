# Oefening PROG4.2: If with 2 boolean operators

# vraagt variablen op.
Leeftijd = input("Geef je leeftijd: ")
Nederlands = input("Nederlands paspoort: ")

# als de leeftijd groter is dan 18
# EN
# als er ja is geantwoord
# krijg je de print
if Leeftijd > str(18) and "ja" in Nederlands:
    print("Gefeliciteerd, je mag stemmen!")
