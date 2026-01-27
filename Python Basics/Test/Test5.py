from random import randint

tools = ['hammer', 'car', 'Diamond hammer', 'gold']

for counter, tool in enumerate(tools):
    print(f'{counter}: {tool}')

print("-"*20)

for counter in range(len(tools)):
    print(f'{counter}: {tools[counter]}')


test_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
for i in range(len(test_matrix)):
    for j in range(len(test_matrix[i])):
        rdm = randint(0, 100)
        test_matrix[i][j] = rdm


print(test_matrix)


n = 10
matrix = list()
for row_idx in range(n):
    row = list()
    for col_ind in range(n):
        if row_idx == col_ind: row.append(1)
        else: row.append(0)
    matrix.append(row)

print(matrix)

colors = ['blue', 'red', 'yellow', 'pink', 'black', 'purple', 'violet', 'green', 'white', 'dark green']

for counter, color in enumerate(colors): print(f'{counter}: {color}')



matrix2 = [[*range(0, 10)], [*range(0, 15)], [*range(0, 4)]]

tt = range(0, 10)

print(tt)



for row_idx, row in enumerate(matrix2):
    for col_ind, col in enumerate(row):
        print(row_idx, col_ind, col)

# 1. Yöntem: Klasik "list()" fonksiyonu kullanımı
# (Okunabilirliği en yüksek olan yöntemdir)
matrix_classic = [list(range(0, 5)), list(range(10, 15)), list(range(20, 25))]

# 2. Yöntem: Yıldız "*" operatörü (Unpacking) kullanımı
# (DİKKAT: Yıldız sayıları döker, dışındaki [] onları listeye çevirir)
matrix_star = [[*range(0, 5)], [*range(10, 15)], [*range(20, 25)]]

# --- VERIFICATION (Doğrulama) ---

# İki matrisin birebir aynı olup olmadığını kontrol edelim
print(f"Are matrices identical? {matrix_classic == matrix_star}")
# Output: True

# --- FOR LOOP EXAMPLE ---

# Oluşturduğumuz matris üzerinde gezme işlemi
# range() artık listeye dönüştüğü için elemanları görebiliriz
print("\nIterating through matrix_star rows:")

for row in matrix_star:
    # Her bir satırı (listeyi) ekrana yazdır
    print(f"Current Row: {row}")

    # İç içe döngü ile sayıları tek tek de alabiliriz
    total = sum(row)
    print(f" -> Sum of this row: {total}")

test_data = [10.5, 11.2, 9.8, None, 11.5, None]

count = sum(1 for value in test_data if value is not None)

counter = 0
tottal = 0

data = [10.5, 11.2, 9.8, 11.5, None]

for val in data:
    counter+=1
    tottal+=1

avg = tottal // count

for idx, value in enumerate(data):
    if value is None: data[idx] = avg

print(data)

[print(item, end=' ') for item in colors]


print(end='\n')

new_list = list()

a = [item for item in colors if 'g' in item]
print(*a)


ttt = list(range(0, 31))

b = [item for item in ttt if item % 2 == 0 if item % 3 == 0]
print (b)