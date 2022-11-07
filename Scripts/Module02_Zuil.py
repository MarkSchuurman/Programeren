# Module 2: Moderatie
# Voordat een bericht ook daadwerkelijk op het stationshalscherm wordt gezet, wordt er door een moderator van de NS
# naar de berichten gekeken. De moderator kan een bericht goed- of afkeuren. Alleen goedgekeurde berichten worden
# gepubliceerd op het stationshalscherm.
#
# Deze module leest de berichten uit het gestructureerde tekstbestand (zoals beschreven bij module 1) in,
# beginnend bij het oudste bericht. Na beoordeling door een moderator wordt het hele bericht (inclusief datum, tijd,
# naam en station) naar een database geschreven. Daarnaast wordt de volgende data toegevoegd:
#
#     of het bericht is goedgekeurd of afgekeurd;
#     de datum en tijd van beoordeling;
#     de naam van moderator die het bericht heeft beoordeeld;
#     het email-adres van de moderator.
#
# Deze module werkt met een Command Line Interface (CLI). Dit mag gewoon gestart worden vanuit PyCharm.
#
# Daarnaast moet voor de werking van deze module een database worden gemaakt en gebruikt. Het ontwerp van deze
# database omvat een conceptueel, een logisch en een fysiek datamodel. De database moet vervolgens worden
# gerealiseerd in PostgreSQL. De gegevens worden gelezen uit het CSV bestand en aangevuld met de moderatorgegevens en
# daarna weggeschreven in de database. Het CSV-bestand wordt daarna leeggemaakt.

from datetime import datetime
import psycopg2 as sql


def time():
    now = datetime.today()
    tijd = datetime.strftime(now, '%m-%d-%Y %H:%M:%S')
    return tijd


def berichten():
    openen = open('zuil_berichen.csv', 'r')
    lines = openen.readlines()
    openen.close()
    lst = []
    naam_mod = str(input(f'Vul hier de naam van de moderator in:'))
    mail_mod = str(input(f'Vul hier het mail adres van de moderator in:'))
    for part in lines:
        splitted_part = part.strip().split(',')
        print(f'{splitted_part[2]} zegt op: {splitted_part[1]} \n{splitted_part[0]} over station {splitted_part[3]}')
        keuring = str(input(f'wordt dit bericht goedgekeurd? Y/N: \n')).lower()
        lst.append([splitted_part[0], splitted_part[1], splitted_part[2], splitted_part[3], keuring, time(), naam_mod,
                    mail_mod])
    return lst


def schrijf(lst):
    openen = open('zuil_berichen.csv', 'w')
    for x in lst:
        lijst = f'{",".join(x)}\n'
        openen.write(lijst)
    openen.close()


schrijf(berichten())

reviews = open('zuil_berichen.csv', 'r')
read = reviews.readlines()
for line in read:
    meningen = line.strip().split(",")
    dbmeningen = (meningen[0], meningen[1], meningen[2], meningen[3])
    dbmoderatie = (meningen[4], meningen[5], meningen[6], meningen[7])

    with sql.connect(
            host='localhost',
            database='NSuilen',
            user='postgres',
            password='Welkom123'
    ) as con:
        with con.cursor() as cur:
            query02 = """INSERT INTO Moderatie values %s"""
            placeholder02 = (tuple(dbmoderatie),)
            cur.execute(query02, placeholder02)

            query01 = """INSERT INTO Review values %s"""
            placeholder01 = (tuple(dbmeningen),)
            cur.execute(query01, placeholder01)


def delete():
    openen = open('zuil_berichen.csv', 'w')
    openen.close()


delete()
