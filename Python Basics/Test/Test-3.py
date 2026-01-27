t = 1, 2, 3
print(type(t), t)
print(t[0])
print(len(t))
print(t[-1:])


test = 38472578375823658723465823469523678

a = []

while test > 0:
    a.append(test%10)
    test //= 10

a.reverse()
print(a[1:len(a)+1:-1])


c = 'ISACC NEWTON'

print(c[:5])

ee = list(c)

print(ee[:])



d = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]

print(d[1:len(d)+1:2])


deneme = 'deneme'
den = 'deneme'
print(deneme is den)

print(den)



# 1. ADIM: Bellekte bir liste oluşur.
# Python bu listeye bir kimlik (ID) verir. Diyelim ki bu listenin adı "KUTU_A" olsun.
# KUTU_A: [0, 0, 0]

# 2. ADIM: 'l' listesi oluşturulur.
# l listesinin ilk elemanı, KUTU_A'nın adresini tutar.
l = [ [0, 0, 0], [1, 1, 1], [2, 2, 2] ]

# Şu an durum şöyle:
# l[0] ---------> KUTU_A ([0, 0, 0])


# 3. ADIM: 'sub' listesi oluşturulur.
# Burada kritik hata/özellik devreye girer.
# l[0]'ı alıp sub'ın içine koyarken, KUTU_A'nın kopyasını değil, ADRESİNİ alırız.
sub = [ l[0], 'Python' ]

# Şu an durum şöyle:
# l[0] ---------> KUTU_A ([0, 0, 0])
# sub[0] -------> KUTU_A ([0, 0, 0])
# İkisi de aynı fiziksel nesneye parmak basıyor!


# 4. ADIM: Değişiklik yapılır (Olay Anı)
sub[0][0] = 100

# Python şunu yapar:
# 1. sub[0]'a git ----> KUTU_A'ya ulaştı.
# 2. KUTU_A'nın ilk elemanını 100 yap.
# KUTU_A artık [100, 0, 0] oldu.


# 5. ADIM: Sonuçları kontrol edelim
print(l[:])   # l[0] hala KUTU_A'yı gösteriyor. KUTU_A değiştiği için bu da değişmiş görünür.
print(sub[:])
# Çıktı: [100, 0, 0]

del l[0]

print(l[:])
print(sub[:])



my_list = [1, 2, 3, 4]

my_list[0:3], my_list[2:4] = my_list[2:4], my_list[0:2]

print(my_list[:])
