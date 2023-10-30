from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowTitle("Programa py")
        self.setMinimumSize(QSize(480,320))
        
        
        etiqueta = QLabel("Soy una etiqueta")
        font = QFont("Fira Code",32)
        
        etiqueta.setFont(font)
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        img = QPixmap(absPath("naturaleza.jpg"))
        etiqueta.setPixmap(img)
        etiqueta.setScaledContents(True)
        
        self.setCentralWidget(etiqueta)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())