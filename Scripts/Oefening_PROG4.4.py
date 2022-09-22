# Oefening PROG4.4: For & strings
# geeft lijst aan
List = ['maandag', 'dinsdag', 'woensdag']
# geeft aantal aan waarnaar het kijk in de lijst
First_Two = List[:3]
# voor elk item in lijst, in dit geval 3
for List in First_Two:
    # print de lijst, en print alleen de eerste 2 karakters van elk item
    print(str(List)[0:2])
