product = 1
while True:
    user_input = input('voer een getal in: ')
    if user_input != 'stop':
        product *= int(user_input)
    else:
        print(f'Als je alle getallen vermenigvuldigd, is het resultaat: {product}')
        break



