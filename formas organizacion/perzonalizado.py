from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
import sys

class Box(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        caja = Box('green')

        self.setCentralWidget(caja)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())