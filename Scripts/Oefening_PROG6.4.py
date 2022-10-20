openen = open("pe_6_4_hardlopers.txt", "a")

import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
name = input("naam: ")
line = f'{s}, {name}\n'
openen.write(line)
