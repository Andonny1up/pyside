from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PySide6.QtCore import Qt
import sys

class Dialogo(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(240,120)
        self.setWindowTitle("Hola")

        layout =  QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("Dialogo de prueba"))

        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        layout.addWidget(botones)



class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resize(430,320)
        boton = QPushButton("Mostrar Dialogo")
        boton.clicked.connect(self.boton_click)

        self.setCentralWidget(boton)

    def boton_click(self):
        dialogo =  Dialogo()
        respuesta = dialogo.exec_()
        if respuesta:
            print("dialogo aceptado")
        else:
            print("dialogo denegado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())