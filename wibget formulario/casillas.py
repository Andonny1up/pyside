from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        casilla =  QCheckBox("casillta")
        casilla.setCheckState(Qt.CheckState.PartiallyChecked)
        casilla.stateChanged.connect(self.estado_cambiado)
        casilla.setEnabled(False)

        print("Activada?", casilla.isChecked())
        print("Activada?", casilla.isTristate())

        self.setCentralWidget(casilla)


    def estado_cambiado(self, estado):
        if Qt.CheckState(estado) == Qt.CheckState.Checked:
            print("cassilla marcada")
        if Qt.CheckState(estado) == Qt.CheckState.Unchecked:
            print("Desmarcada")
        if Qt.CheckState(estado) == Qt.CheckState.PartiallyChecked:
            print("pARTIAL")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())