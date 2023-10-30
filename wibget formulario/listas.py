from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()

        lista = QListWidget()
        lista.addItems(["Op 1","Op 2","Op 3"])
        lista.currentItemChanged.connect(self.item_cambiado)

        print(lista.currentItem())

        self.setCentralWidget(lista)

    def item_cambiado(self, item):
        print("Nuevo Item", item.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())