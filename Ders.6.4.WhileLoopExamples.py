""" sayilar = [1, 3, 5, 7, 9, 12, 19, 21] """

""" i = 0
while i < len(sayilar):
    print(sayilar[i])
    i += 1
 """

""" baslangic = int(input("Başlangıç Değerini Giriniz...: "))
bitis = int(input("Bitiş Değerini Giriniz...: "))


i = baslangic
while i < bitis:
    i += 1
    if i % 2 == 1:
        print(i) """


""" i = 100
while i > 0:
    print(i)
    i -= 1
 """


""" numbers = []


i = 0

while i < 5:
    sayi = int(input("Sayı Giriniz...: "))
    numbers.append(sayi)
    i += 1

numbers.sort()
print(numbers)
 """


urunler = []

adet = int(input("Kaç Adet Ürün Eklemek İstiyorsunuz...?: "))

i = 0

while i < adet:
    name = input("Ürünün Adını Giriniz..: ")
    price = int(input("Ürünün Fiyatını Giriniz...: "))
    urunler.append({"name": name, "price": price})
    i += 1

for urun in urunler:
    print(f"Ürün Adı: {urun['name']} Ürünün Fiyatı: {urun['price']}")
