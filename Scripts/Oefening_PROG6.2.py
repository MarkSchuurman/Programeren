def pretty_print():
    open_file = open("pe_6_2_kaartnummers.txt", "r")
    file_readline = open_file.readlines()

    for line in file_readline:
        number_name = line.split(",")
        number = number_name[0].strip()
        name = number_name[1].strip()
        print(f'{name} heeft kaartnummer: {number}')

pretty_print()
