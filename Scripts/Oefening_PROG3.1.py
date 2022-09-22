# Oefening PROG3.1: Getallen, strings & conversion

cijferPROJA = 6.5
cijferPROG = 8.9
cijferMOD = 7.1
gemiddelde = (cijferPROJA + cijferPROG + cijferMOD) / 3
beloning = (cijferPROJA + cijferPROG + cijferMOD) * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'
print(overzicht)