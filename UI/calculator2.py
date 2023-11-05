from PyQt6 import QtWidgets
import sys
from MainWindow import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesaplama)
        self.ui.btn_cikarma.clicked.connect(self.hesaplama)
        self.ui.btn_carpma.clicked.connect(self.hesaplama)
        self.ui.btn_bolme.clicked.connect(self.hesaplama)
        self.ui.btn_tumIslemler.clicked.connect(self.hesaplama)

    def hesaplama(self):
        sender = self.sender().text()
        result = 0

        if self.ui.txt_sayi1.text() and self.ui.txt_sayi2.text():
            sayi1 = int(self.ui.txt_sayi1.text())
            sayi2 = int(self.ui.txt_sayi2.text())

            if sender == "Toplama":
                result = sayi1 + sayi2
                self.ui.toplamaSonuc.setText(
                    "Tekil İşlem: İki Sayının Toplamının Sonucu: " + str(result)
                )

            elif sender == "Çıkarma":
                result = sayi1 - sayi2
                self.ui.cikarmaSonuc.setText(
                    "Tekil İşlem: İki Sayının Farklarının Sonucu: " + str(result)
                )

            elif sender == "Çarpma":
                result = sayi1 * sayi2
                self.ui.carpmaSonuc.setText(
                    "Tekil İşlem: İki Sayının Çarpımlarının Sonucu: " + str(result)
                )

            elif sender == "Bölme":
                result = sayi1 / sayi2
                self.ui.bolmeSonuc.setText(
                    "Tekil İşlem: İki Sayının Bölümlerinin Sonucu: " + str(result)
                )

            elif sender == "Tüm İşlemler":
                result = sayi1 + sayi2
                self.ui.toplamaSonuc.setText(
                    "Tüm İşlemler: İki Sayının Toplamlarının Sonucu: " + str(result)
                )
                result = sayi1 - sayi2
                self.ui.cikarmaSonuc.setText(
                    "Tüm İşlemler: İki Sayının Farklarının Sonucu: " + str(result)
                )
                result = sayi1 * sayi2
                self.ui.carpmaSonuc.setText(
                    "Tüm İşlemler: İki Sayının Çarpımlarının Sonucu: " + str(result)
                )
                result = sayi1 / sayi2
                self.ui.bolmeSonuc.setText(
                    "Tüm İşlemler: İki Sayının Bölümlerinin Sonucu: " + str(result)
                )


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())


app()
