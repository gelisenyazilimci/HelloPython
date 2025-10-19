import random

a = 65

random_number = random.randrange(1, 100)
print("Oluşan Rastgele sayı bulma oyunu")
print("10 tahmin hakkı vardır her oyuncun")
print(''.join(['-' for _ in range(40)]))
user_guest = input("1 ile 100 arasında bir sayı tahmin et: ")
counter = 1

while counter != 11:
    if counter >= 2:
        user_guest = input("Tekrardan 1 ile 100 arasında bir sayı tahmin et: ")
        int(user_guest)
    try:
        value = int(user_guest)
    except ValueError:
        print("That's not an integer.")
        exit()
    if value < random_number:
        counter += 1
        print("Rastgele Sayıdan Daha Küçük Bir Sayı Girdin!")
    if value > random_number:
        counter += 1
        print("Rastgele Sayıdan Daha Büyük Bir Sayı Girdin!")
    if value == random_number: break


print(''.join(['-' for _ in range(40)]))
if int(user_guest) == random_number:
    print(f"Sayıyı Bildin! {"Random Oluşan Sayı: ", random_number, " ", "Senin Girdiğin Sayı: ", user_guest, " ", "Şu kadar deneme içerisinde buldum: ", counter}")
else: print(f"Sayıyı Bilemedin Ve {counter} Tahmin Etme Sınırına Ulaştın.Oluşan Random Sayı: {random_number}")


