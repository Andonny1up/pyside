from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()

        texto =  QLineEdit()
        texto.setMaxLength(15)
        texto.setPlaceholderText("Escribe Máximo 15 caracteres")
        texto.textChanged.connect(self.texto_cambiado)
        texto.returnPressed.connect(self.enter_presionado)

        self.setCentralWidget(texto)

    
    def texto_cambiado(self,texto):
        print("Texto cambiado:",texto)

    
    def enter_presionado(self):
        texto = self.centralWidget().text()
        print("Enter presionado, texto:", texto)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())