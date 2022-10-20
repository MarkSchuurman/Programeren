# Oefening PROG5.3: Functie met if
# maakt de functie aan
def lang_genoeg():
    # vraagt een variabele op
    lente_van_de_gebruiker = int(input("vul hier je lengte in: "))
    # als de variabele groter is dan 120 word het volgende gedaan
    if lente_van_de_gebruiker > 120:
        return "Je bent lang genoeg voor de attractie!"
    # als de variabele kleiner is dan 120 dan word het volgende gedaan:
    else:
        return "Sorry, je bent te klein!"


# als je de functie print maar de functie heeft geen return dan krijg je none omdat je iets print wat niet aangeduid
# is de functie heeft geen "waarde" tot dat je de waarde returnt dus als je functie geen return heeft dan hoef je hem
# ook niet uit te printen, maar alleen de functie aa nte roepen en een return en een print horen bij elkaar,
# dus als je geen return hebt in de functie hoef je ook geen print uit te voeren. en omgekeerd natuurlijk ook
print(lang_genoeg())
