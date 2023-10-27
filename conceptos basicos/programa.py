from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit
from PySide6.QtCore import QSize
import sys

# app = QApplication(sys.argv)
# window = QMainWindow()
# window.setWindowTitle("Hola Mundo")
# button = QPushButton("setso")

# window.setCentralWidget(button)



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Programa py")
        button = QPushButton("setso")
        # button.clicked.connect(self.boton_click)
        # button.pressed.connect(self.boton_press)
        # button.released.connect(self.boton_released)
        button.setCheckable(True)
        button.clicked.connect(self.boton_alternado)
        texto = QLineEdit()
        texto.textChanged.connect(self.texto_modificado)
        self.setCentralWidget(texto)

        # self.setMaximumSize(QSize(480,320))
        # self.setMinimumSize(QSize(480,320))
        self.setFixedSize(QSize(480,320))

        self.button = button
        self.texto = texto

    def texto_modificado(self):
        texto_recuperado = self.texto.text()
        self.setWindowTitle(texto_recuperado)

    def boton_click(self):
        print("BOTON")

    
    def boton_press(self):
        print("PRESS")

    def boton_released(self):
        print("RELESS")

    def boton_alternado(self,valor):
        if valor:
            self.button.setText("Estoy activado")
        else:
            self.button.setText("Estoy Desactivado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())