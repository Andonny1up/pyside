from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        numero = QDoubleSpinBox()
        # numero.setMinimum(0)
        # numero.setMaximum(10)
        numero.setRange(0,10)
        numero.setSingleStep(2)
        numero.setPrefix("$")
        numero.setSuffix("bs")
        numero.setValue(8)
        print(numero.value())


        numero.valueChanged.connect(self.valor_cambiado)


        self.setCentralWidget(numero)

    def valor_cambiado(self, numero):
        print("Valor cambiado", numero)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())