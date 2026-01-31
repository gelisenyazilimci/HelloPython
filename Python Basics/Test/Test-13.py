import math


def dN (*number):
    print(number)
    return number[0] / 2
ll = [3,5,7,10,20,30]
al = list()
for x in ll:
    al.append(dN(x))
print(al)
def ddN (*number):
    print(number)
    return list(n / 2 for n in number)
xx = []
xx.extend(ddN(*ll))
print(xx)


sq = [*map(lambda x: math.pow(x, 2), ll)]
print(sq)

usernames = [{'ad': 'Zeynep', 'yas': 25}, {'ad': 'Ahmet', 'yas': 40}, {'ad': 'Mehmet', 'yas': 18}]
# Soru: Bu listeyi YAŞA göre küçükten büyüğe nasıl sıralarız?
# Lambda'nın görevi: Listenin içindeki her bir sözlüğü alıp, sadece 'yas' değerini teslim etmek.
usernames.sort(key=lambda x: x['yas'])
print(usernames)