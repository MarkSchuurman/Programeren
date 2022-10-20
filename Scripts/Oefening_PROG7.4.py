tafels = range(1, 11)
for tafel in tafels:
    for aantal_keer in range(1, 11):
        print(f'{aantal_keer:2} x {tafel:2} = {aantal_keer * tafel:>3}')
