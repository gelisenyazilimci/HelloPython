from time import monotonic

# monotic veya perf_counter() kullanilabilir

start = monotonic()

l1 = range(100)
l2 = range(100)

end = monotonic()

print(f'elapsed: {end - start}')

print('-' * 50)

data = [('item1', 10, 100), ('item2', 5, 25), ('item3', 100, 0.25)]
d = dict()
for item in data:
    d[item[0]] = {'num sold:': item[1], 'unit price:': item[2]}
print(d)
schema = ('widget', 'num_sold', 'unit_price')
x = []
for row in data:
    print(row[0] ,{*zip(schema[1:], row)})



widgets = [f'w{i}' for i in range(1, 21)]
skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]
def xy (*x):
    return zip(*x)
print(*xy(widgets, skus))

