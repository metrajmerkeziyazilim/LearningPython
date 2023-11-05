import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator App")
        self.setGeometry(200, 200, 700, 700)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1:")
        self.lbl_sayi1.move(50, 30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150, 30)
        self.txt_sayi1.resize(150, 30)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2:")
        self.lbl_sayi2.move(50, 80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150, 80)
        self.txt_sayi2.resize(150, 30)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Toplama")
        self.btn_topla.move(150, 130)
        self.btn_topla.clicked.connect(self.hesaplama)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkarma")
        self.btn_cikar.move(150, 170)
        self.btn_cikar.clicked.connect(self.hesaplama)

        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.setText("Çarpma")
        self.btn_carpma.move(150, 210)
        self.btn_carpma.clicked.connect(self.hesaplama)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText("Bölme")
        self.btn_bolme.move(150, 250)
        self.btn_bolme.clicked.connect(self.hesaplama)

        self.btn_tumIslemler = QtWidgets.QPushButton(self)
        self.btn_tumIslemler.setText("Tüm İşlemler")
        self.btn_tumIslemler.move(350, 130)
        self.btn_tumIslemler.clicked.connect(self.hesaplama)

        self.lbl_toplamaSonuc = QtWidgets.QLabel(self)
        self.lbl_toplamaSonuc.setText("Sonuç:")
        self.lbl_toplamaSonuc.move(150, 290)
        self.lbl_toplamaSonuc.setFixedWidth(300)  # Genişliği 300 piksel olarak ayarla

        self.lbl_cikarmaSonuc = QtWidgets.QLabel(self)
        self.lbl_cikarmaSonuc.setText("Sonuç:")
        self.lbl_cikarmaSonuc.move(150, 330)
        self.lbl_cikarmaSonuc.setFixedWidth(300)  # Genişliği 300 piksel olarak ayarla

        self.lbl_carpmaSonuc = QtWidgets.QLabel(self)
        self.lbl_carpmaSonuc.setText("Sonuç:")
        self.lbl_carpmaSonuc.move(150, 370)
        self.lbl_carpmaSonuc.setFixedWidth(300)  # Genişliği 300 piksel olarak ayarla

        self.lbl_bolmeSonuc = QtWidgets.QLabel(self)
        self.lbl_bolmeSonuc.setText("Sonuç:")
        self.lbl_bolmeSonuc.move(150, 410)
        self.lbl_bolmeSonuc.setFixedWidth(300)  # Genişliği 300 piksel olarak ayarla

    def hesaplama(self):
        sender = self.sender().text()
        result = 0

        if self.txt_sayi1.text() and self.txt_sayi2.text():
            sayi1 = int(self.txt_sayi1.text())
            sayi2 = int(self.txt_sayi2.text())

            if sender == "Toplama":
                result = sayi1 + sayi2
                self.lbl_toplamaSonuc.setText(
                    "Tekil İşlem: İki Sayının Toplamının Sonucu: " + str(result)
                )

            elif sender == "Çıkarma":
                result = sayi1 - sayi2
                self.lbl_cikarmaSonuc.setText(
                    "Tekil İşlem: İki Sayının Farklarının Sonucu: " + str(result)
                )

            elif sender == "Çarpma":
                result = sayi1 * sayi2
                self.lbl_carpmaSonuc.setText(
                    "Tekil İşlem: İki Sayının Çarpımlarının Sonucu: " + str(result)
                )

            elif sender == "Bölme":
                result = sayi1 / sayi2
                self.lbl_bolmeSonuc.setText(
                    "Tekil İşlem: İki Sayının Bölümlerinin Sonucu: " + str(result)
                )

            elif sender == "Tüm İşlemler":
                result = sayi1 + sayi2
                self.lbl_toplamaSonuc.setText(
                    "Tüm İşlemler: İki Sayının Toplamlarının Sonucu: " + str(result)
                )
                result = sayi1 - sayi2
                self.lbl_cikarmaSonuc.setText(
                    "Tüm İşlemler: İki Sayının Farklarının Sonucu: " + str(result)
                )
                result = sayi1 * sayi2
                self.lbl_carpmaSonuc.setText(
                    "Tüm İşlemler: İki Sayının Çarpımlarının Sonucu: " + str(result)
                )
                result = sayi1 / sayi2
                self.lbl_bolmeSonuc.setText(
                    "Tüm İşlemler: İki Sayının Bölümlerinin Sonucu: " + str(result)
                )


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())


app()
