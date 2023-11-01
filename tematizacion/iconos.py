from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet
import sys
# import qtawesome as qta # solo para pyside2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        icono = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        # icono =  qta.icon("fa5.save")
        boton = QPushButton(icono,"Boton Guardar")
        self.setCentralWidget(boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
