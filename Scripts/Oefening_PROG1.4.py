# Oefening PROG1.4: Boolean expressions
# Schrijf booleaanse expressies die van de variabelen van Practice Exercise 1.3 evalueren of:
a = 6
b = 7
c = (a + b) / 2
voornaam = 'Bart'
tussenvoegsel = 'van'
achternaam = 'Eijkelenburg'
mijnnaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam

# 6.75 groter is dan A en kleiner B.
print(6.75 > a and 6.75 < b)

# de lengte van mijnnaam even groot is als de som van de lengte van voornaam, tussenvoegsel en achternaam.
print(len(mijnnaam) == len(voornaam) + len(tussenvoegsel) + len(achternaam))

# de lengte van mijnnaam minstens 5 maal groter is dan variabele c.
print(len(mijnnaam) >= c * 5)

# de waarde van variabele tussenvoegsel voorkomt in de waarde van variabele achternaam.
print(tussenvoegsel in achternaam)

# The len() function returns the number of items in an object.
#
# When the object is a string, the len() function returns the number of characters in the string.
