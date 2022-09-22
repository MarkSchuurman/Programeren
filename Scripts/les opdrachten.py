List = [4, 0, 1, -2]


def function():
    result = max(List) - min(List)
    return result


print("the range is", function())



Lijst = ('one', 'two', 'three')
x = Lijst[0]
y = Lijst[1]
temp = x
x = y
y = temp
print("x = ", x)
print("y = ", y)
print(str(Lijst))
