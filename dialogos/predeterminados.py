from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PySide6.QtCore import Qt
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

    def boton_click(self):
        # dialogo =  QMessageBox.question(self,"Cuestion","Setso?")
        # dialogo =  QMessageBox.about(self,"Acerca de","El sistema es setsoso \nyes.") -- information-warning
        # dialogo =  QMessageBox.critical(self,"Error","El sistema es setsoso \nyes.")

        dialogo =  QMessageBox.warning(
            self,"Aviso","¿Seguro que deseas aplicar estos cambios?",
            buttons=QMessageBox.Apply | QMessageBox.Cancel)

        if dialogo == QMessageBox.Apply:
            print("si")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())