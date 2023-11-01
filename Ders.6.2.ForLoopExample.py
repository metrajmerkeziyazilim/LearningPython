""" sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
 """
"""3'ÜN KATI OLAN SAYILAR"""
""" for sayi in sayilar:
    if sayi % 3 == 0:
        print("Üç'e Tam Bölünen Sayı:", sayi)
 """

""" toplam = 0
for sayi in sayilar:
    toplam += sayi """

"""print("Listedeki Sayıların Toplamı: ", toplam)"""


"""TEK SAYILARIN KARELERİ"""
""" for sayi in sayilar:
    if sayi % 2 == 1:
        print(sayi**2) """


""" sehirler = [
    "kocaeli",
    "istanbul",
    "ankara",
    "izmir",
    "rize",
]

for city in sehirler:
    if len(city) <= 5:
        print(city)
 """

urunler = [
    {"name": "Samsung S6", "price": "3000"},
    {"name": "Samsung S7", "price": "3001"},
    {"name": "Samsung S8", "price": "3002"},
    {"name": "Samsung S9", "price": "3003"},
    {"name": "Samsung S10", "price": "3004"},
    {"name": "Samsung S11", "price": "3005"},
]
toplam = 0
for product in urunler:
    print(product["price"])

for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat

print(toplam)
