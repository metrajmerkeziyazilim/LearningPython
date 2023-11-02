import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6 import QtWidgets


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Application")
    win.setGeometry(1400, 500, 1000, 1000)
    win.setWindowIcon(QIcon("2023-11-02_20-13-13.png"))

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Adınızı Giriniz..:")
    lbl_name.move(100, 100)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınızı Giriniz..:")
    lbl_surname.move(100, 150)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(225, 100)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(225, 150)

    def clicked(self):
        print("Butona Tıklandı. Alınan Name Özelliği: " + txt_name.text())
        print("Butona Tıklandı. Alınan Surname Özelliği: " + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(225, 200)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec())


window()
