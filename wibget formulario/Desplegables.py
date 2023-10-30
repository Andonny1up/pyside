from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()

        desplegable = QComboBox()
        desplegable.addItems(["Op 1","Op 2", "Op 3"])
        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_cambiado)

        print("Indice actual", desplegable.currentIndex())
        print("Texto actual", desplegable.currentText())

        self.setCentralWidget(desplegable)

    def indice_cambiado(self, indice):
        print("Nuevo Indice",indice)

    def texto_cambiado(self, texto):
        print("Nuevo Texto", texto)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())