import math
import random
from functools import reduce
from math import pi

def action (*iterable):
    return sum(iterable) / len (iterable)

#print(action(*range(0, 11), *range(1, 10)))
#print(*range(0, 11))


def test (a, b, *c, d):
   return [a, b, c, d]
#print(test(1, 2, 3, 4, 5, 6, d = 7))

def x (a, d, **dd):
    return [a, d, dd]

#print(x(a = 31, d = 32, dd = {'x': 10, 'y': 30}))


x = lambda x, y: x+y
#print(x(31, 69))

xx = lambda x, y, z: max(x, y, z) + math.fsum([x, y, z])
#print(xx(31, 31, 31))



table = lambda row, col: [[i * j for j in range(1, col+1)] for i in range(1, row+1)]
#print(table(3, 3))


f = lambda x = 10, y = 20: math.fmod(x, y)
#print(f())


def xx (*num):
    if len(num) == 1: return int(num[0])
    ortalama = sum([x for x in map(float, num)]) / len(num)
    #print(*map(float, num))
    return ortalama

#print(xx(1, 2, 3, 4, 5))

ll = ['a','a','b','c']
# x = list
# y = string
unique = reduce(lambda x, y: x if y in x else x + [y] ,ll, [])
print(*unique)


print([round(100, -2)])

print(pi)

print(math.floor(1.9))

print(round(123456.213123, -3))


sss = sorted([1, 10 , 2 ,23, 4, 1, 2, 3], key=str)
print(type(sss))


nnnn = [{"isim":"Bur", "yaş":31, "ülke":"TR",}]
print(type(nnnn[0]))



print(sorted([["I", "K", "l", "m"], ["A", "G", "f", "E"], ["a", "B", "c", "D"]]))
print(ord(sorted([["I", "K", "l", "m"], ["A", "G", "f", "E"], ["a", "B", "c", "D"]])[0][0]))
print(list(reversed(["a", "B", "c", "D"])))
