import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        self.setAutoFillBackground(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(500, 500, 500, 500)

        hlayout1 = QtWidgets.QHBoxLayout()

        hlayout1.addWidget(Color("red"))
        hlayout1.addWidget(Color("blue"))
        hlayout1.addWidget(Color("green"))
        hlayout1.setContentsMargins(50, 50, 50, 20)

        hlayout2 = QtWidgets.QHBoxLayout()

        hlayout2.addWidget(Color("pink"))
        hlayout2.addWidget(Color("gray"))
        hlayout2.setSpacing(50)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        """layout = QtWidgets.QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("blue"), 1, 0)
        layout.addWidget(Color("green"), 0, 2)
        layout.addWidget(Color("yellow"), 3, 3)
        """
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vlayout)
        self.setCentralWidget(central_widget)


def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


app()
