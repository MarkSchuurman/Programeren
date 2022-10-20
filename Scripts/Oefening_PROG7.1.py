# Oefening PROG7.1: Decision control
def seizoen(maand):
    if maand <= 0 or maand > 12:
        return f'Ongeldig'
    elif maand in range(3, 6):
        return f'Lente'
    elif maand in range(6, 9):
        return f'Zomer'
    elif maand in range(9, 12):
        return f'Herfst'
    else:
        return f'Winter'


print(seizoen(6))
