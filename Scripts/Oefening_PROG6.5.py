def gemiddelde():
    zin = str(input("Geef hier een zin in: "))
    words = zin.split()
    if len(words) != 0:
        gem = sum(len(word) for word in words) / len(words)
        print(f'het gemiddelde aantal letters per woord is: {gem:.1f}')
    else:
        print("je moet iets typen lul!")

gemiddelde()