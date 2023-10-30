from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QGridLayout
from PySide6.QtCore import Qt
import sys

class Box(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        cuadricula = QGridLayout()
        cuadricula.addWidget(Box("orange"),0,0)
        cuadricula.addWidget(Box("purple"),1,1)
        cuadricula.addWidget(Box("magenta"),0,1)
        cuadricula.addWidget(Box("magenta"),2,2)

        widget = QWidget()
        widget.setLayout(cuadricula)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())