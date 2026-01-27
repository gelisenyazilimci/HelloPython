num = [*range(0, 11)]
x = list(map(str, num))
print(type(x[1]))


names = ['  Maria  selam ben', ' John', 'Bulut ']
print(list(map(str.strip, names)))

print([*range(1, 5)])

numbers = [*range(1, 5)]
print([*map(lambda x: x ** 2 , numbers)])

names = ('maria', 'ali', 'bulut', 'ozan')
u = tuple([*map(str.capitalize, names)])
print(u)

names = ("Ali", "Su", "Can", "Zeynep", "Oya")  # Tuple

# İsmi 3 harften uzun olanları alıp KÜME (Set) yapalım
long_names = tuple(filter(lambda x: len(x) > 3, names))

print(long_names)