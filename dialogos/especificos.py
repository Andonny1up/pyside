from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QInputDialog, QFontDialog, QColorDialog
from PySide6.QtCore import Qt, QTranslator, QLibraryInfo
from PySide6.QtGui import QIcon
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resize(430,320)
        self.setWindowIcon(QIcon(absPath("icon.png")))

        boton = QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_click)

        self.setCentralWidget(boton)

        self.boton = boton

    def boton_click(self):
        # fichero, _ =  QFileDialog.getSaveFileName(self,"Abrir archivo",".")
        # print(fichero)
        # valor, confirmacion = QInputDialog.getText(self,"Titulo","Texto")
        # valor, confirmacion = QInputDialog.getInt(self,"Titulo","Entero")
        # valor, confirmacion = QInputDialog.getDouble(self,"Titulo","Decimal")
        # valor, confirmacion = QInputDialog.getItem(self,"Titulo","Colores",["Rojo","Azul","Verde"],editable=False)
        confirmado, fuente = QFontDialog.getFont(self)
        if confirmado:
            self.boton.setFont(fuente)
        color = QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f'background-color:{color.name()}')
        


if __name__ == '__main__':
    app = QApplication(sys.argv)

    traductor = QTranslator(app)
    traducciones = QLibraryInfo.location(QLibraryInfo.LibraryPath.TranslationsPath)
    traductor.load("qt_es",traducciones)
    app.installTranslator(traductor)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())