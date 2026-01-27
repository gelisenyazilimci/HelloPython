import math as mth
from numbers import Integral

(a, b, c) = ((), [], {1})


a, b = b, a


print(type(b))


myNum = -1.69

myNumTransInt = int(mth.floor(myNum))

print(myNumTransInt)



def myCeil (x) -> int:
    i = int(x)
    if i <= 0: return i
    else: return i if i == x else i + 1


def myFloor (x) -> Integral:
    i = int(x)
    if x >= 0: return i
    else: return i if i == x else i - 1


print(myCeil(2.50))
print(type(Integral))


def do_while (stuf, condition):
    while condition(stuf()):
       pass

testList = ["a","b","c"]

for letter in range(1, len(testList) + 1):
    print(letter)



testtt = list(range(10, 100, 20))



for index in enumerate(testtt):
    print(index)

for (index, number) in enumerate(testtt):
    print(index, number)
