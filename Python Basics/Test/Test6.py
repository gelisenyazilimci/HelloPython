from statistics import fmean

data = [10.5, 11.2, 9.8, None, 11.5, None]

count = sum(1 for val in data if val is not None)
total = sum(count for val in data if val is not None)
avg = total / count
data = [val if val is not None else int(avg) for val in data]

print(data)


data2 = [*range(0, 40, 3)]
print(data2)
fmean_data2 = fmean(data2)
print(f'average: {fmean_data2}')



data3 = [*range(100, 600, 100)]

for last_element in range(len(data3)):
    print(f'{data3.pop() if len(data3) is not 0 else ""}')

print(len(data3))

print(globals())


test_data = {'elma': 10, 'armut': 20, 'muz': 30}

first_key = next(iter(test_data))
print(first_key)
print(test_data[first_key])

test_keys = list(test_data.keys())
test_items = list(test_data.items())

print(test_keys)
print(test_data.values())


testx = {'a': 200, 'v':200, 'c': 100, 'd': 10}


# .items() iki farklı şekilde kullanılabiliyor işe yarayan bir fonksiyon
for t in testx.items(): # .items() tuple olarak çıktı vermemizi sağlar!
    print(t)

for k, v in testx.items():
    print(f'{k} = {v}') # .items() key ve value olarak ayrıştırma da yapabilir


karisik_sozluk = {
    "apple": ['elma', 'elmaa'],
    "bilgisayar": "computer",
    "keyboard": "klavye",
    "mouse": "fare",
    "ekran": "screen",
    "yazılım": "software",
    "developer": "geliştirici",
    "network": "ağ",
    "veri tabanı": "database",
    "algorithm": "algoritma",
    "artificial intelligence": "yapay zeka",
    "güvenlik": "security",
    "cloud": "bulut",
    "sunucu": "server",
    "istemci": "client",
    "function": "fonksiyon",
    "variable": "değişken",
    "döngü": "loop",
    "koşul": "condition",
    "library": "kütüphane",
    "framework": "çatı",
    "kaynak kodu": "source code",
    "derleyici": "compiler",
    "interpreter": "yorumlayıcı",
    "hata ayıklama": "debugging",
    "arayüz": "interface",
    "user": "kullanıcı",
    "password": "şifre",
    "kimlik doğrulama": "authentication",
    "yetkilendirme": "authorization",
    "dosya": "file",
    "klasör": "folder",
    "bellek": "memory",
    "işlemci": "processor",
    "depolama": "storage",
    "backup": "yedekleme",
    "güncelleme": "update",
    "version": "sürüm",
    "açık kaynak": "open source",
    "lisans": "license",
    "protokol": "protocol",
    "internet": "internet",
    "tarayıcı": "browser",
    "arama motoru": "search engine",
    "website": "web sitesi",
    "alan adı": "domain name",
    "hosting": "barındırma",
    "bandwidth": "bant genişliği",
    "latency": "gecikme",
    "throughput": "iş hacmi"
}

for i in karisik_sozluk:
    print(i, karisik_sozluk[i])


print(list(karisik_sozluk.values()))
print(*karisik_sozluk.values())

last_dictionary = {"k1":10,"k2": [10,20,30,40,50],"k3":"string","k4": {"a":100,"b":200}}

print(last_dictionary['k2'][3])
print(last_dictionary['k4']['b'])

