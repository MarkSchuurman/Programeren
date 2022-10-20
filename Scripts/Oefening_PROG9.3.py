# Oefening PROG9.3: ASCII

def code(invoerstring):
    for char in invoerstring:
        getal = ord(char)
        nieuw_getal = getal + 3
        nieuwe_letter = chr(nieuw_getal)
        print(nieuwe_letter, end="")


code(str(input(f'Voer uw naam, uw begin station en uw eind station door: ')))
