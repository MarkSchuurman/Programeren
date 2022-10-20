# Final Assignment PROG3: Bagagekluizen


print(f'1: Ik wil weten hoeveel kluizen nog vrij zijn \n'
      f'2: Ik wil een nieuwe kluis \n'
      f'3: Ik wil even iets uit mijn kluis halen \n'
      f'4: Ik geef mijn kluis terug \n')

keuze = int(input(f'Uw Keuze:'))
if keuze < 1 or keuze > 4:
    print(f'Ongeldige invoer')


def aantal_kluizen_vrij():
    openen = open("fa_kluizen.txt", "rt")
    readlines_file = openen.readlines()
    length_file = len(readlines_file)
    openen.close()
    open_lines = int(12 - length_file)
    return open_lines


def nieuwe_kluis():
    keuzes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    openen = open('fa_kluizen.txt', 'r')
    kluizen = openen.readlines()
    openen.close()

    for kluis in kluizen:
        num_kluis = int(kluis.split(';')[0])
        if num_kluis in keuzes:
            keuzes.remove(num_kluis)

    if len(keuzes) > 0:
        code = input(f'Voer uw code in: ')
        if len(code) >= 4:
            f = open('fa_kluizen.txt', 'a')
            f.write(f'{keuzes[0]};{code}\n')
            f.close()
            return f'Uw kluisnummer is: {keuzes[0]} met code: {code}'
        else:
            return f'Uw code is niet lang genoeg!'
    else:
        return f'Helaas zijn er geen kluizen beschikbaar'


def kluis_openen():
    print(f'[Kluis openen]')
    try:
        kluis_num = int(input(f'Kluisnummer: '))
    except ValueError:
        return f'Het kluisnummer moet een getal zijn!'
    kluis_code = input(f'Kluiscode: ')
    f = open('fa_kluizen.txt', 'r')
    kluizen = f.readlines()
    f.close()

    for kluis in kluizen:
        kluis_info = kluis.split(';')
        if (int(kluis_info[0]) == kluis_num) and (kluis_info[1].strip() == kluis_code):
            return f'Uw gegevens zijn correct!'

    return f'Helaas zijn uw gegevens niet correct'


def kluis_teruggeven():
    print(f'[Kluis teruggeven]')
    try:
        kluis_num = int(input(f'Kluisnummer: '))
    except ValueError:
        return f'Het kluisnummer moet een getal zijn!'
    kluis_code = input('Kluiscode: ')

    openen = open('fa_kluizen.txt', 'r')
    kluizen = openen.readlines()
    openen.close()

    kluis_bestaat = False

    for kluis in kluizen:
        kluis_info = kluis.split(';')
        if (int(kluis_info[0]) == kluis_num) and (kluis_info[1].strip() == kluis_code):
            kluis_bestaat = True

    if kluis_bestaat:
        openen = open('fa_kluizen.txt', 'w')
        for kluis in kluizen:
            kluis_info = kluis.split(';')
            if int(kluis_info[0]) != kluis_num:
                openen.write(kluis)
        openen.close()
        return f'Uw kluis is teruggegeven!'
    else:
        return f'Uw kluis is niet gevonden'


if keuze == 1:
    print(f'Er zijn nog {aantal_kluizen_vrij()} kluizen vrij.')
elif keuze == 2:
    print(nieuwe_kluis())
elif keuze == 3:
    print(kluis_openen())
elif keuze == 4:
    print(kluis_teruggeven())

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import builtins
# import collections
# import sys
# import traceback

# """
# Programming
# Final assignment 3: Bagagekluizen
# (c) 2021 Hogeschool Utrecht,
# Tijmen Muller en
# Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)
# Opdracht:
# Werk onderstaande functies uit.
# Voeg commentaar toe om je code toe te lichten.
# Lever je werk in op Canvas als alle tests slagen.
# """
#
#
# def aantal_kluizen_vrij():
#     openen = open("fa_kluizen.txt", "rt")
#     readlines_file = openen.readlines()
#     length_file = len(readlines_file)
#     openen.close()
#     open_lines = int(12 - length_file)
#     return open_lines
#
#
# def nieuwe_kluis():
#     keuzes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     openen = open('fa_kluizen.txt', 'r')
#     kluizen = openen.readlines()
#     openen.close()
#
#     for kluis in kluizen:
#         num_kluis = int(kluis.split(';')[0])
#         if num_kluis in keuzes:
#             keuzes.remove(num_kluis)
#
#     if len(keuzes) > 0:
#         code = input(f'Voer uw code in: ')
#         if len(code) >= 4:
#             f = open('fa_kluizen.txt', 'a')
#             f.write(f'{keuzes[0]};{code}\n')
#             f.close()
#             return keuzes[0]
#         else:
#             return -1
#     else:
#         return -2
#
#
# def kluis_openen():
#     print(f'[Kluis openen]')
#     try:
#         kluis_num = int(input(f'Kluisnummer: '))
#     except ValueError:
#         return f'Het kluisnummer moet een getal zijn!'
#     kluis_code = input(f'Kluiscode: ')
#     f = open('fa_kluizen.txt', 'r')
#     kluizen = f.readlines()
#     f.close()
#
#     for kluis in kluizen:
#         kluis_info = kluis.split(';')
#         if (int(kluis_info[0]) == kluis_num) and (kluis_info[1].strip() == kluis_code):
#             return True
#
#     return False
#
#
# def kluis_teruggeven():
#     print(f'[Kluis teruggeven]')
#     try:
#         kluis_num = int(input(f'Kluisnummer: '))
#     except ValueError:
#         return f'Het kluisnummer moet een getal zijn!'
#     kluis_code = input('Kluiscode: ')
#
#     openen = open('fa_kluizen.txt', 'r')
#     kluizen = openen.readlines()
#     openen.close()
#
#     kluis_bestaat = False
#
#     for kluis in kluizen:
#         kluis_info = kluis.split(';')
#         if (int(kluis_info[0]) == kluis_num) and (kluis_info[1].strip() == kluis_code):
#             kluis_bestaat = True
#
#     if kluis_bestaat:
#         openen = open('fa_kluizen.txt', 'w')
#         for kluis in kluizen:
#             kluis_info = kluis.split(';')
#             if int(kluis_info[0]) != kluis_num:
#                 openen.write(kluis)
#         openen.close()
#         return f'Uw kluis is teruggegeven!'
#     else:
#         return f'Uw kluis is niet gevonden'
#
#
# def development_code():
#     # Breid deze code uit om het keuzemenu te realiseren:
#     print(f'1: Ik wil weten hoeveel kluizen nog vrij zijn \n'
#           f'2: Ik wil een nieuwe kluis \n'
#           f'3: Ik wil even iets uit mijn kluis halen \n'
#           f'4: Ik geef mijn kluis terug \n')
#
#
# def module_runner():
#     # development_code()  # Comment deze regel om je 'development_code' uit te schakelen
#     __run_tests()  # Comment deze regel om de HU-tests uit te schakelen
#
#
# """
# ==========================[ HU TESTRAAMWERK ]================================
# Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
# """
#
#
# def __my_assert_args(function, args, expected_output, check_type=False):
#     """
#     Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
#     Optioneel wordt ook het return-type gecontroleerd.
#     """
#     argstr = str(args).replace(',)', ')')
#     output = function(*args)
#
#     # Controleer eerst het return-type (optioneel)
#     if check_type:
#         msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
#         assert type(output) is type(expected_output), msg
#
#     # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
#     if str(expected_output) == str(output):
#         msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
#               f"in plaats van {expected_output} (type {type(expected_output).__name__})"
#     else:
#         msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
#
#     if type(expected_output) is float and isinstance(output, (int, float, complex)):
#         # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
#         assert round(output - expected_output, 7) == 0, msg
#     else:
#         assert output == expected_output, msg
#
#
# def __out_of_input_error():
#     raise AssertionError("Fout: er werd in de functie vaker om input gevraagd dan verwacht.")
#
#
# def __my_test_file():
#     return "fa_testkluizen.txt"
#
#
# def __check_line_in_testfile(line, testfile=__my_test_file()):
#     with open(testfile, 'r') as dummy_file:
#         for file_line in dummy_file.readlines():
#             if line.strip() == file_line.strip():
#                 return True
#
#     return False
#
#
# def __create_test_file(safes, testfile=__my_test_file()):
#     kluis_mv_ev = 'kluis' if len(safes) == 1 else 'kluizen'
#     print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(safes)} {kluis_mv_ev}... ", end="")
#
#     try:
#         with open(testfile, 'w') as dummy_file:
#             for number, code in safes:
#                 dummy_file.write(f"{number};{code}\n")
#     except:
#         print(f"\nFout: bestand {testfile} kon niet worden aangemaakt. Python-error:")
#         print(traceback.format_exc())
#         sys.exit()
#
#     print("Klaar.")
#
#
# def __create_fake_open(original_open):
#     def fake_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
#         return original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors,
#                              newline=newline, closefd=closefd, opener=opener)
#
#     return fake_open
#
#
# def test_aantal_kluizen_vrij():
#     function = aantal_kluizen_vrij
#
#     case = collections.namedtuple('case', 'safes')
#     testcases = [case(((11, "6754"),)),
#                  case(((11, "6754"), (1, "geheim"), (12, "z@terd@g"))),
#                  case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
#                        (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000")))]
#
#     for test in testcases:
#         __create_test_file(test.safes)
#
#         original_open = builtins.open
#         builtins.open = __create_fake_open(original_open)
#
#         try:
#             expected_output = 12 - len(test.safes)
#             __my_assert_args(function, (), expected_output, check_type=True)
#         finally:
#             builtins.open = original_open
#
#
# def test_nieuwe_kluis():
#     function = nieuwe_kluis
#
#     case = collections.namedtuple('case', 'safes simulated_input possible_outputs')
#     testcases = [case(((11, "6754"), (12, "z@terd@g")), ["geheim"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
#                  case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
#                        (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000")), ["geheim"],
#                       [-2]),
#                  case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
#                        (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (12, "0000")), ["geheim"], [10]),
#                  case(((1, "0000"), (3, "0000"), (5, "0000"), (8, "0000"), (10, "0000"), (12, "0000"),
#                        (2, "0000"), (4, "0000"), (6, "0000"), (9, "0000"), (11, "0000")), ["geheim"], [7]),
#                  case(((2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000"),
#                        (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000")), ["geheim"], [1]),
#                  case(((1, "0000"), (3, "0000")), ["abc"], [-1])]
#
#     for test in testcases:
#         __create_test_file(test.safes)
#
#         original_open = builtins.open
#         builtins.open = __create_fake_open(original_open)
#
#         original_input = builtins.input
#         simulated_input = test.simulated_input.copy()
#         simulated_input.reverse()
#         builtins.input = lambda prompt="": simulated_input.pop() if len(simulated_input) > 0 else __out_of_input_error()
#
#         try:
#             output = function()
#
#             assert isinstance(output,
#                               int), f"Fout: {function.__name__}() geeft {type(output).__name__} in plaats van int. Check evt. {__my_test_file()}"
#             assert output in test.possible_outputs, f"Fout: {function.__name__}() geeft {output}, maar mogelijke outputs zijn alleen: {test.possible_outputs}"
#
#             # if all possible safenumbers are positive, a new safenumber should be registered by now
#             if all(possible_safe_number > 0 for possible_safe_number in test.possible_outputs):
#                 free_safes = aantal_kluizen_vrij()
#                 expected_free_safes = 12 - (len(test.safes) + 1)
#
#                 msg = f"Fout: {function.__name__}() geeft aan dat een nieuwe kluis (nummer {output}) gereserveerd is, maar " \
#                       f"daarna geeft aantal_kluizen_vrij() {free_safes} ipv {expected_free_safes}. Check evt. {__my_test_file()}"
#
#                 assert free_safes == expected_free_safes, msg
#
#             if output >= 0:
#                 msg = f"Fout: {function.__name__}() geeft aan dat kluis {output} gereserveerd is (ww: '{test.simulated_input[-1]}'), " \
#                       f"maar {__my_test_file()} bevat daarna geen regel met \"{output};{test.simulated_input[-1]}\"."
#
#                 assert __check_line_in_testfile(f"{output};{test.simulated_input[-1]}"), msg
#
#         except AssertionError as ae:
#             raise AssertionError(
#                 f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {test.simulated_input}.") from ae
#         finally:
#             builtins.input = original_input
#             builtins.open = original_open
#
#
# def test_kluis_openen():
#     function = kluis_openen
#
#     case = collections.namedtuple('case', 'safes simulated_input expected_output')
#     testcases = [case(((11, "6754"), (12, "z@terd@g")), ["11", "1234"], False),
#                  case(((11, "6754"), (12, "z@terd@g")), ["11", "6754"], True),
#                  case(((11, "6754"), (12, "z@terd@g")), ["12", "z@terd@g"], True),
#                  case(((11, "6754"), (12, "z@terd@g")), ["10", "6754"], False),
#                  case(((11, "geheim"),), ["1", "geheim"], False),
#                  case(((12, "geheim"),), ["2", "geheim"], False)]
#
#     for test in testcases:
#         __create_test_file(test.safes)
#
#         original_open = builtins.open
#         builtins.open = __create_fake_open(original_open)
#
#         original_input = builtins.input
#         simulated_input = test.simulated_input.copy()
#         simulated_input.reverse()
#         builtins.input = lambda prompt="": simulated_input.pop() if len(simulated_input) > 0 else __out_of_input_error()
#
#         try:
#             __my_assert_args(function, (), test.expected_output, check_type=True)
#         except AssertionError as ae:
#             raise AssertionError(
#                 f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {test.simulated_input}.") from ae
#         finally:
#             builtins.input = original_input
#             builtins.open = original_open
#
#
# def test_kluis_teruggeven():
#     function = kluis_teruggeven
#
#     case = collections.namedtuple('case', 'safes simulated_input expected_output')
#     testcases = [case(((11, "6754"), (12, "z@terd@g")), ["11", "1234"], False),
#                  case((), ["1", "geheim"], False),
#                  case(((11, "6754"), (12, "z@terd@g")), ["12", "z@terd@g"], True),
#                  case(((11, "6754"), (12, "z@terd@g")), ["11", "6754"], True),
#                  case(((11, "6754"),), ["11", "6754"], True),
#                  case(((11, "geheim"),), ["1", "geheim"], False),
#                  case(((12, "geheim"),), ["2", "geheim"], False)]
#
#     for test in testcases:
#         __create_test_file(test.safes)
#
#         original_open = builtins.open
#         builtins.open = __create_fake_open(original_open)
#
#         original_input = builtins.input
#         simulated_input = test.simulated_input.copy()
#         simulated_input.reverse()
#         builtins.input = lambda prompt="": simulated_input.pop() if len(simulated_input) > 0 else __out_of_input_error()
#
#         try:
#             __my_assert_args(function, (), test.expected_output, check_type=True)
#
#             if test.expected_output:  # safe should be available again
#                 free_safes = aantal_kluizen_vrij()
#                 expected_free_safes = 12 - (len(test.safes) - 1)
#
#                 msg = f"Fout: {function.__name__}() geeft aan dat kluis (nummer {test.simulated_input[0]}) vrijgegeven is, maar " \
#                       f"daarna geeft aantal_kluizen_vrij() {free_safes} ipv {expected_free_safes}."
#
#                 assert free_safes == expected_free_safes, msg
#
#         except AssertionError as ae:
#             raise AssertionError(
#                 f"{ae.args[0]}\n -> Info: gesimuleerde input voor deze test: {test.simulated_input}.") from ae
#         finally:
#             builtins.input = original_input
#             builtins.open = original_open
#
#
# def __run_tests():
#     """ Test alle functies. """
#     test_functions = [test_aantal_kluizen_vrij,
#                       test_nieuwe_kluis,
#                       test_kluis_openen,
#                       # Uncomment de regel hieronder om ook de optionele functie kluis_teruggeven te testen:
#                       # test_kluis_teruggeven
#                       ]
#
#     try:
#         for test_function in test_functions:
#             func_name = test_function.__name__[5:]
#
#             print(f"\n======= Test output '{test_function.__name__}()' =======")
#             test_function()
#             print(f"Je functie {func_name} werkt goed!")
#
#         print("\nGefeliciteerd, alles lijkt te werken!")
#         print("Lever je werk nu in op Canvas...")
#
#     except AssertionError as e:
#         print(e.args[0])
#     except Exception as e:
#         print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
#         print(traceback.format_exc())
#
#
# if __name__ == '__main__':
#     module_runner()
