from math import sqrt


vex = [(x, y) for x in range(2) for y in range(2)]
print(vex)
print('-'*20, end='\n')
mag = [float(sqrt(pow(vec[0], 2 + pow(vec[1], 2)))) for vec in vex]
print(mag)


wid = [f'w{item+1}' for item in range(4)]
sales = [10, 5, 15, 0]
dic = { wid[i]: sales[i] if sales[i] > 0 else 31 for i in range(len(wid)) }
print(dic)


er = 0

try:
    file = open('test.txt', "r")
except FileNotFoundError:
    print(f"Variable {str("x")} not defined")
except TabError:
    print("Tab ERROR")
    er+=1
finally:
    print(f"ERROR = {er}" )


l = ["a","b","c","c"]
t = [1234567890]
print(*enumerate(l, 1))
#print(type(l))
#print())
it = iter(l)

for idx_val in [enumerate(l)]:
    print(*idx_val)

print("\n")

te = ["a", "b", "c", "d", "e", "f", "g"]
print(*map(str.upper, te))



