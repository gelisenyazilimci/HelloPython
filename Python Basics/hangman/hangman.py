import json
import random

with open('words.json', 'r', encoding='utf-8') as data: words = json.load(data)

random_number = random.randrange(0, len(words["kelimeler"]))

secret_word = words["kelimeler"][random_number]

secret_word_length = len(secret_word)

max_wrong_guesses = 9

wrong_guesses_count = 0

wrong_guesses = []

display = ["_"] * secret_word_length

print(words["kelimeler"])


while wrong_guesses_count < max_wrong_guesses:
    user_input = input("Bir karakter giriniz: ").lower()
    if not user_input.isalpha() or len(user_input) != 1 or type(user_input) != str:
        print("Lütfen SADECE BİR HARF giriniz.")
        continue
    else:
        if user_input in display or user_input in wrong_guesses:
            print(f"'{user_input}' harfini zaten denemiştin!")
            continue

        harf_bulundu = False

        for i in range(secret_word_length):
            if secret_word[i] == user_input:
                display[i] = user_input
                harf_bulundu = True

        if harf_bulundu:
            print(f"Harika! '{user_input}' harfi kelimede var.")
            print(" ".join(display))
        else:
            print(f"Maalesef! '{user_input}' harfi kelimede yok.")
            wrong_guesses.append(user_input)
            wrong_guesses_count += 1
            print(f"Yanlış Girilen Harfler: {', '.join(wrong_guesses)}")

    if "_" not in display:
        print("\n🎉 TEBRİKLER! Kelimeyi doğru tahmin ettin! 🎉")
        print(f"Kelime: {secret_word}")
        break


if "_" in display:
    print("\n😢 Üzgünüm, deneme hakkın bitti!")
    print(f"Doğru kelime: {secret_word}")