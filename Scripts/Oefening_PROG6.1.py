def convert(graden_cel):
    return (graden_cel * 1.8) + 32

def table():
    print(f'{"F":^7}{"C":^9}')
    for x in range(-30, 41, 10):
        print(f'{convert(x):>6} {x:>6}')


table()
