from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from PySide6.QtCore import Qt, QTranslator, QLibraryInfo
from PySide6.QtGui import QIcon, QAction
from pathlib import Path
import sys
import random



def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class Subventana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resize(240,120)
        self.setWindowTitle("subventana")
        etiqueta = QLabel(f"soy una subventana... {random.randint(0,100)}")
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resize(430,320)
        self.setWindowIcon(QIcon(absPath("../dialogos/icon.png")))
        self.setWindowTitle("Ventana principal")

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        boton_mostrar = QPushButton("Mostrar Subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)

    def mostrar_subventana(self):
        self.subventana =  Subventana()
        self.subventana.show()
        



if __name__ == '__main__':
    app = QApplication(sys.argv)

    traductor = QTranslator(app)
    traducciones = QLibraryInfo.location(QLibraryInfo.LibraryPath.TranslationsPath)
    traductor.load("qt_es",traducciones)
    app.installTranslator(traductor)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())