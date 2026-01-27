import math
from math import exp

my_string = "Python Ogreniyorum"
t = my_string[4]
print(t)

my_new_string = "ProgramlamayaMerhabaDedik" #ramla
tt = my_new_string[4:8]
print(tt)

my_last_string = "Afyonkarahisarlilastiramadiklarimizdanmisiniz"
ttt = my_last_string[::-1]
print(ttt)

print(type(4 + 12.2 + 48))
print(5 + 7 * 12)

# Bu listeyi en az 2 farkli yoldan olusturunuz: [1,3,"a"]

a = [1, 2, 'a']
aa = list((1, 2, "a"))
print(a)
print(aa)

my_list = [3.14,4,[2,3,"b"],True]

aaa = my_list[2][2]
print(aaa)

my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}
d = list(my_dictionary["kk2"][1].values())[0]
dd = my_dictionary["kk2"][1]["k21"]
ddd = next(iter(my_dictionary["kk2"][1].values()))
print(d)
print(dd)
print(ddd)

my_list_to_be_set = [3,4,9,3,21,22,4,3,9,10,21,22]
translate_to_set = set(my_list_to_be_set)

print(translate_to_set)

my_list = [*range(10, 80, 10)]
#for l in my_list:
    #if int(math.exp(math.log(l) - math.log(6)) + 0.0000001) * 6 == l: print(l)


print(int(math.exp(math.log(36) - math.log(6)) + 0.0000001) * 6 == 36)
sonuc_listesi = [l for l in my_list if int(math.exp(math.log(l) - math.log(6)) + 0.0000001) * 6 == l]
print(" ".join(map(str, sonuc_listesi)))