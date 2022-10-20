# Module 1: Zuil
#
# Op een zuil op een willekeurig NS-station kunnen reizigers hun bericht van maximaal 140 karakters invoeren.
# Het bericht moet worden opgeslagen in een tekstbestand met een logische structuur.
# Sla de onderstaande gegevens op in een gestructureerd tekstbestand:
#
# het bericht; de datum en tijd van het bericht; de naam van de reiziger – als de reiziger geen naam invult,
# gebruik dan als naam ‘anoniem’; het station – deze locatie van de zuil mag in de module zelf worden vastgelegd op
# basis van een random choice van drie stations. De computer (jouw python computer programma) kiest dan één station
# uit deze lijstlijst downloaden  en dat station wordt dan gekoppeld aan het bericht.
#
# Deze module werkt met een Command Line Interface (CLI). Dit mag gewoon gestart worden vanuit PyCharm.
from datetime import datetime
import random


def time():
    now = datetime.today()
    tijd = datetime.strftime(now, '%m-%d-%Y %H:%M:%S')
    return tijd


def naam():
    name = str(input(f'Voer hier uw naam in: ')).strip()
    if name == "":
        name = "anoniem"
    return name


def station():
    stations = ['Arnhem', 'Almere', 'Amersfoort']
    return random.choice(stations)


while True:
    bericht = input(f'Bericht: ')
    if len(bericht) > 140:
        print(f'je bericht is te lang')
        continue
    else:
        string = f'{bericht},{time()},{naam()},{station()}\n'
        openen = open('zuil_berichen.csv', 'a')
        openen.write(string)
        openen.close()
    break
