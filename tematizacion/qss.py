from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QStyle, QWidget, QLabel, QFormLayout,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QPlainTextEdit, QVBoxLayout)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet
from pathlib import Path
import sys
# import qtawesome as qta # solo para pyside2

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class EditorQss(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.resize(480,320)
        self.setWindowTitle("Editor Qss nen vivo")

        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet("""
            background-color: #212121;
            color: #e9e9e9;
            
        """)
        self.editor.textChanged.connect(self.actualizar_estilos)

        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        self.setLayout(layout)
        self.show()

    def actualizar_estilos(self):
        qss =  self.editor.toPlainText()
        try:
            self.parent.setStyleSheet(qss)
        except:
            pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        formulario =  QFormLayout()
        formulario.addRow("QCheckBox",QCheckBox())
        formulario.addRow("QRadioButton",QRadioButton())
        etiqueta = QLabel("QLabel")
        etiqueta.setObjectName("etiqueta")
        formulario.addRow(etiqueta)
        formulario.addRow("QLabel", QLabel("QLabel"))
        formulario.addRow("QPushButton",QPushButton("Setso An"))
        formulario.addRow("QLineEdit",QLineEdit())
        formulario.addRow("QSpinBox",QSpinBox())

        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)

        self.setStyleSheet("""
        QMainWindow {background-color: #212121}
        QLabel {color: #e9e9e9}
        QPushButton {
            background-color: orange;
            font-family: "Arial";
            font-size: 14px;
        }
        #etiqueta {
            background-color: cyan;
            padding: 10px;
            color: black;
        }
        """)

        self.editorQSS = EditorQss(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
