from random import randint, shuffle

s = ['abi', 'selam']
ss = set()
for i, v in enumerate(s):
    ss.update(v)
    print(v)
    print(i)
    print(ss)

print(ss)

print(type(ss), len(ss))

print('a' in ss , 'p' in ss)

print(ss)

sss = {0x0321, 0x0322, 0x0321, 0x0323, 0x851}
print(sss)
print(type(sss))


test_list = [*range(0, 110, 10)]

for i in test_list:
    if i is 40:
        print(True)
        break
    else: print(i)



test = [*range(0, 100, 6)]
print(test)

shuffle(test)
print(test)