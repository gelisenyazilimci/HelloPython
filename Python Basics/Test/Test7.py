import math

str1 = 'AAAAAB'
str2 = 'AAA'
if str1 + str2 != str2 + str1: print("")
else:
    print(str1[:math.gcd(len(str1), len(str2))])

test = ['aaa']
test.extend([31, '313131', 313])
print(test)