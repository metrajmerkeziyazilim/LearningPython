""" sayi = float(input("Sayı Giriniz.....: "))

result = (sayi > 0) and (sayi <= 100)

if result:
    print(f"Girilen Sayı 0-100 Arasındadır ve Girilen Sayı: {result}")
else:
    print(f"Girilen Sayı 0-100 Arasında Değildir ve Girilen Sayı: {result}")
 """


number = int(input("Sayı Giriniz...:"))

if number > 0:
    if number % 2 == 0:
        print(f"Girilen Sayı Pozitif Çift Sayıdır.")
    elif number % 2 == 1:
        print(f"Girilen Sayı Pozitif Tek Sayıdır.")
if number < 0:
    if abs(number) % 2 == 0:
        print(f"Girilen Sayı Negatif Çift Sayıdır.")
    elif abs(number) % 2 == 1:
        print(f"Girilen Sayı Negatif Tek Sayıdır.")
else:
    print(f"Yaptığın Hareketlere Dikkat Et :)")
