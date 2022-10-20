# Oefening PROG9.2: Random
import random


def monopolyworp():
    dobbelsteen = [1, 2, 3, 4, 5, 6]
    worpen = []
    worp01 = random.choice(dobbelsteen)
    worp02 = random.choice(dobbelsteen)
    worpen.append((worp01, worp02))
    worp_totaal = worp01 + worp02
    worp_print = f'{worp01} + {worp02} = {worp_totaal} '
    print(worp_print)

    while True:
        if worp01 == worp02:
            worp01 = random.choice(dobbelsteen)
            worp02 = random.choice(dobbelsteen)
            worpen.append((worp01, worp02))
            worp_print = f'{worp01} + {worp02} = {worp_totaal} '
            print(worp_print)

            if worp01 == worp02:
                worp01 = random.choice(dobbelsteen)
                worp02 = random.choice(dobbelsteen)
                worpen.append((worp01, worp02))
                worp_print = f'{worp01} + {worp02} = {worp_totaal} '
                print(worp_print)

                if worp01 == worp02:
                    print(f'{worp01} + {worp02} = Direct naar de gevangenis!')
                else:
                    print(worp_print)
        print(worpen)
        break

    # print(worp_steen01)
    # print(worp_steen02)
    # print(totaal_worp)


for i in range(10000):
    monopolyworp()
