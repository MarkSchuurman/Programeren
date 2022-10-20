import math

x1 = int(input(f'X-positie van coördinaat 1 (x1):'))
y1 = int(input(f'X-positie van coördinaat 1 (y1):'))
x2 = int(input(f'X-positie van coördinaat 2 (x2):'))
y2 = int(input(f'X-positie van coördinaat 2 (y2):'))

uitkomst = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
resultaat = round(uitkomst, 4)
print(f'Afstand tussen de coördinaten ({x1},{y1}) en ({x2},{y2}): {resultaat}')
