from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sys
from _msgboxForm import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):
        result = QMessageBox.question(
            self,
            "Close Application",
            "Are you sure to do that?",
            buttons=(
                QMessageBox.StandardButton.Ok
                | QMessageBox.StandardButton.Cancel
                | QMessageBox.StandardButton.Ignore
            ),
            defaultButton=QMessageBox.StandardButton.Cancel,
        )

        if result == QMessageBox.StandardButton.Ok:
            print("Yes Clicked")
            QtWidgets.QApplication.quit()
        elif result == QMessageBox.StandardButton.Ignore:
            print("Uyarı Yok Sayıldı...")
        else:
            print("Çıkış Reddedildi")

        """msg = QMessageBox()
        msg.setWindowTitle("Close Application")
        msg.setText("Are Your Sure To Exeminate The Program?")
        msg.setIcon(QMessageBox.Icon.Warning)

        ok_button = msg.addButton(QMessageBox.StandardButton.Ok)

        msg.setStandardButtons(
            QMessageBox.StandardButton.Ok
            | QMessageBox.StandardButton.Cancel
            | QMessageBox.StandardButton.Ignore
        )

        msg.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msg.setDetailedText("Detailsdfgsdfhgdsgfhdfghdfghdfghdfghdfgs...")
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec()
        print(x)"""

    """def popup_button(self, i):
        print(i.text())

        if i.text() == "OK":
            print("OK Tuşuna Tıkladın... ve Uygulama Kapandı.")
            QtWidgets.QApplication.quit()
        elif i.text() == "Ignore":
            print("Ignore Tuşuna Tıkladın...")
            QtWidgets.QApplication.quit()
        elif i.text() == "Cancel":
            print("Cancel Tuşuna Tıkladın...")
        else:
            print("Canın Cennete Dostum  Tuşuna Tıkladın...")"""


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()

sys.exit(app.exec())
