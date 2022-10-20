def pretty_print():
    file_open = open("pe_6_2_kaartnummers.txt", "r")
    file_readlines = file_open.readlines()
    # print(file_readlines)
    line_count = len(file_readlines)

    file_open.seek(0)
    lst = []
    for x in file_open:
        number_name = x.split(",")
        lst.append(number_name)

    toob = lst.index(max(lst)) + 1

    print(f'deze file telt {line_count} regels')
    print(f'het grootste kaartnummer is: {max(lst)[0]}')
    print(f'en dat staat op regel {toob}')
    file_open.close()


pretty_print()
