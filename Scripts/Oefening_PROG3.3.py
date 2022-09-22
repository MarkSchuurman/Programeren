# Oefening PROG3.3: Input/output

# Schrijf een programma dat de gebruiker vraagt om zijn uurloon,
# het aantal uur dat hij of zij gewerkt heeft en dat daarna het salaris uitprint.
uurloon = float(input('Wat verdien je per uur: '))
uren = int(input('Hoeveel uur heb je gewerkt: '))

print(str(uren) + ' uur werken levert €' + str(uren * uurloon) + ' op')