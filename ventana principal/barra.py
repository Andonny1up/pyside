from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStatusBar, QToolBar
from PySide6.QtCore import Qt, QTranslator, QLibraryInfo
from PySide6.QtGui import QIcon, QAction
from pathlib import Path
import sys


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.resize(430,320)
        self.setWindowIcon(QIcon(absPath("../dialogos/icon.png")))
        self.setStatusBar(QStatusBar(self))

        self.construir_menu()
        self.construir_herramientas()

    def construir_herramientas(self):
        herramientas = QToolBar("Barra de herramientas")
        herramientas.addAction(QIcon(absPath("../dialogos/icon.png")),"Salir",self.close)
        herramientas.addAction(self.accion_info)

        self.addToolBar(herramientas)

    def construir_menu(self):
        menu = self.menuBar()

        menu_archivo = menu.addMenu("&MenuA")
        menu_archivo.addAction("&Prueba")
        sub_menu = menu_archivo.addMenu("&Submenu")
        sub_menu.addAction("Subopcion &2")

        menu_archivo.addSeparator()
        menu_archivo.addAction(QIcon(absPath("../dialogos/icon.png")),"Salir",self.close, "Ctrl+Q")

        menu_ayuda = menu.addMenu("Ayuda")
        accion_info = QAction("&Informacion",self)
        accion_info.setIcon(QIcon(absPath("../dialogos/icon.png")))
        accion_info.setShortcut("Ctrl+I")
        accion_info.setStatusTip("Informacion perrona")
        accion_info.triggered.connect(self.mostrar_info)

        menu_ayuda.addAction(accion_info)

        self.accion_info = accion_info

    
    def mostrar_info(self):
        QMessageBox.information(self,"Informacion","Texto Informativo")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    traductor = QTranslator(app)
    traducciones = QLibraryInfo.location(QLibraryInfo.LibraryPath.TranslationsPath)
    traductor.load("qt_es",traducciones)
    app.installTranslator(traductor)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())