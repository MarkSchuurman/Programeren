# Oefening PROG9.5: Input/output


while True:
    try:
        loon = float(input(f'Uurloon: '))
        uren = int(input(f'Gewerkte uren: '))
        print(f'{loon * uren} is uw salaris')
        break
    except NameError:
        print(f'vul hier een getal in')
        continue
    except ValueError:
        print(f'vul hier een getal in')
        continue