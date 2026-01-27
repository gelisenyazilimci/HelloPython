def test (num1):
    if 31 + num1 < 0:
        raise ValueError("Çekilecek miktar negatif olamaz!")
    return 31 + num1

print(test(-32))