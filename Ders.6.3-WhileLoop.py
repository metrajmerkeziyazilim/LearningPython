# 1-100 arası sayıları yazalım
""" x = 0

while x < 100:
    if x % 2 == 1:
        print(f"Sayı Tektir: {x}")
    else:
        print(f"Çift Sayıdır: {x}")
    x += 1

print("Bitti")
 """


name = ""

while not name.strip():
    name = input("İsminizi Giriniz...: ")

print(f"Merhaba, {name} Nasılsın?")
