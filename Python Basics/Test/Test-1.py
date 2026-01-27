import math

a = float(math.pi)
b = float(10.1)

tol = 0.001

gercek_fark = abs(a - b)

sonuc = (gercek_fark <= tol)

print(f"Gerçek Fark: {gercek_fark}")
print(f"Tolerans Payı: {tol}")
print(f"İki sayı birbirine yakın mı? {sonuc}")