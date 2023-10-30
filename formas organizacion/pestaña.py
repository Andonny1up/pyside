from PySide6.QtWidgets import QApplication, QMainWindow, QLabel,QWidget, QTabWidget
from PySide6.QtCore import Qt
import sys

class Box(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f'background-color: {color}')


class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        
        tabs = QTabWidget()
        tabs.addTab(Box("orange"),"Naranja")
        tabs.addTab(Box("blue"),"Verde")
        tabs.addTab(Box("red"),"Rojo")
        # widget = QWidget()
        # widget.setLayout(layout)

        tabs.setTabPosition(QTabWidget.TabPosition.West) #eAST
        tabs.setMovable(True)

        self.setCentralWidget(tabs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())