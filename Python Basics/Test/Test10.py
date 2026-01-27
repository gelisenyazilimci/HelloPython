import random

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

print(*('True' for i in my_dictionary.values() if i == 'c'))

if 'c' in my_dictionary.values():
    print('True')

my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}
if 'a' in  my_other_dictionary.keys(): print('True')

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
for num in my_numbers:
    if num & 1: print("odd")
    else: print("even")

for num in my_numbers:
    checker = num % 2
    if checker == 0:
        print("Even")
    else: print("Odd")

print([num for num in my_numbers if num % 2 == 0])

metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]

print(random.choice(metal_list))
for i in range(len(metal_list)):
    rmd = random.randint(0, i)
    print(metal_list[rmd])


age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]

name, age = zip(*age_name_list)
print(age)


test_set = {1, 2, 3}
test_set.update([31, 10, 8, *range(0, 31, 2)])
print(test_set)