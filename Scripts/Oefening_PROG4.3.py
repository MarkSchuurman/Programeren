#Oefening PROG4.3: If/else

# vraagt variablen op.
Leeftijd = input("Geef je leeftijd: ")
Nederlands = input("Nederlands paspoort: ")

# als de leeftijd groter is dan 18
# EN
# als er ja is geantwoord
# krijg je de print
if Leeftijd > str(18) and "ja" in Nederlands:
    print("Gefeliciteerd, je mag stemmen!")
# als het niet voldoet aan de "if" dan wordt het volgende uitgevoerd
else:
    print("Gefeliciteerd, je mag NIET stemmen!")