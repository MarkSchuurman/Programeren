# Oefening PROG5.5: Functie met list-parameter en for-loop
def kwadraten_som(grondgetal):
    som = 0
    for x in grondgetal:
        if x > 0:
            som += x ** 2
    return som


print(kwadraten_som([5, 5, -8]))
