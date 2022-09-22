# Oefening PROG4.5: For, if & numbers

# maakt de lijst
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# voor elk nummer in List
for (num) in List:
    # als nummer door 2 gedeeld kan blijven worden tot er 0 overblijft
    if num % 2 == 0:
        # print nummer en achter het nummer plaats een spatie
        print(num,end=" ")
