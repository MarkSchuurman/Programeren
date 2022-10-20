# Oefening PROG8.2: While-loop & strings

while True:
    woord = input(f'Geef een string van vier letters: ')
    if len(woord) == 4:
        print(f'Inlezen van correcte string: {woord} is geslaagd')
        break
    else:
        print(f'{woord} heeft {len(woord)} letters')