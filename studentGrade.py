"""Fonksiyon Tanımalamaları"""


def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi, ogrenciSoyadi = liste[0].split(" ")

    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = int((not1 + not2 + not3) / 3)

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 65:
        harf = "CC"
    else:
        harf = "FF"

    return (
        "Öğrenci Adı:"
        + "   Soyadı:"
        + "    Öğrenci Harf Notu:\n"
        + "    "
        + ogrenciAdi
        + " "
        + "     "
        + ogrenciSoyadi
        + "             "
        + harf
        + "\n"
    )


def ortalamalari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğrenci Adı Giriniz:")
    soyad = input("Öğrenci Soyadı Giriniz:")
    not1 = input("Not-1:")
    not2 = input("Not-2:")
    not3 = input("Not-3:")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n")


def notlari_kayitet():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


def kayit_sil(ogrenci_adi):
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("sinav_notlari.txt", "w", encoding="utf-8") as file:
        for line in lines:
            if not line.startswith(ogrenci_adi):
                file.write(line)


def kayit_silme_sor():
    ogrenci_adi = input("Silmek İstediğiniz Öğrencinin Adını Giriniz: ")
    confirmation = input(
        f"{ogrenci_adi} adlı öğrencinin kayıtlarını silmek istediğinize emin misiniz? "
    )

    if confirmation.lower() == "y":
        kayit_sil(ogrenci_adi)
        print(f"{ogrenci_adi} Adlı Öğrenci Başarıyla Silindi.")
    else:
        print(f"{ogrenci_adi} Adlı Öğrencinin Kaydı Silinemedi")


"""Döngü İşlemlerinin Yapıldığı Yer"""
while True:
    islem = input(
        "1- Notları Oku: \n2- Not Gir: \n3- Notları Kayıt Et: \n4- Kayıt Sil: \n5- Çıkış Yap: "
    )

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayitet()
    elif islem == "4":
        kayit_silme_sor()
    else:
        break
