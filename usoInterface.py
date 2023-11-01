from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle, QMessageBox, QWidget
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet
from interfaces.mainwindow import Ui_MainWindow
from interfaces.subventana import Ui_Form
import sys
# import qtawesome as qta # solo para pyside2

class Subventana(QWidget, Ui_Form):
   def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.mostrar_subventana)
        self.actionSalir.triggered.connect(self.close)

        self.subventana = Subventana()

    def mostrar_subventana(self):
        self.subventana.label.setText(self.lineEdit.text())
        self.subventana.show()

    def mostrar_mensaje(self):
        QMessageBox.information(self,"Hola",f"El contenido del texto: {self.lineEdit.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
