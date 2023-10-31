from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resize(430,320)
        boton = QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_click)

        self.setCentralWidget(boton)

    def boton_click(self):
        dialogo =  QMessageBox(self)
        dialogo.setWindowTitle("Titulo de ejemplo")
        dialogo.setText("Esto es un dialogo de prueba")
        dialogo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        dialogo.button(QMessageBox.Ok).setText("Aceptar")
        dialogo.button(QMessageBox.Cancel).setText("Cancelar")

        dialogo.setIcon(QMessageBox.Question)


        respuesta = dialogo.exec_()
        if respuesta == QMessageBox.Ok:
            print("Aceptado")
        else:
            print("Denegado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())