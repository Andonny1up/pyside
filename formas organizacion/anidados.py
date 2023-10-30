from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
import sys

class Box(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        layout_hor = QHBoxLayout()
        layout_ver1 = QVBoxLayout()
        layout_ver2 = QVBoxLayout()

        layout_hor.addWidget(Box('green'))
        layout_hor.addLayout(layout_ver1)
        layout_hor.addLayout(layout_ver2)

        layout_ver1.addWidget(Box('blue'))
        layout_ver1.addWidget(Box('red'))

        layout_ver2.addWidget(Box('orange'))
        layout_ver2.addWidget(Box('magenta'))
        layout_ver2.addWidget(Box('purple'))
        
        widget = QWidget()
        widget.setLayout(layout_hor)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())