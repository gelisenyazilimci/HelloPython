def action (*iterable):
    return sum(iterable) / len (iterable)

print(action(*range(0, 11), *range(1, 10)))
print(*range(0, 11))


def test (a, b, *c, d):
   return [a, b, c, d]
print(test(1, 2, 3, 4, 5, 6, d = 7))

def x (a, d, **dd):
    return [a, d, dd]


print(x(a = 31, d = 32, dd = {'x': 10, 'y': 30}))


x = lambda x, y: x+y
print(x(31, 69))