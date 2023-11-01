import random

sayi = random.randint(1, 100)
can = int(input("Kaç Defa Denemek İstiyorsun...?"))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin ET...: "))

    if sayi == tahmin:
        print(
            f"Tebrikler {sayac}. defada Tahmin Ettiniz, Tahmin Ettiğiniz Sayi: {sayi}, Toplam Puanınız: {100-5*sayac}"
        )
        break
    elif sayi > tahmin:
        print("Arttır...")
    else:
        print("Azalt....")

    if hak == 0:
        print("Hakkınız Bitti")
