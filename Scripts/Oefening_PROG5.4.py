# Oefening PROG5.4: Functie met if met meerdere condities
# maakt een functie aan
def new_password():
    # maakt de varia
    old_password01 = str(input("Fill in your old password: "))
    new_password01 = str(input("Fill in your new password: "))
    # met not worden de operators omgekeerd, isalpha kijkt of alle karakters letter zijn deze zal false geven
    # # maar door de not wordt dit true
    if (old_password01 != new_password01) and (len(new_password01) >= 6) and not new_password01.isalpha():
        return True
    # elif len(new_password01) <= 6:
    #     return True
    # elif str("0123456789") in new_password01:
    #     return True
    else:
        return False


if new_password():
    print("Succesvol")
else:
    print("Niet succesvol")
