from PySide6 import QtWidgets
from ui_calculadora import Ui_Calculadora as form_class

class PantallaCalculadora(QtWidgets.QMainWindow, form_class):
    """Clase básica que carga la interfaz generada por QtDesigner"""

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def opera(self):
        # Método que se llamará al hacer clic en el botón de operar
        pass

    def verifica(self):
        # Método que se llamará al hacer clic en el botón de operar
        pass

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = PantallaCalculadora()
    window.show()
    sys.exit(app.exec_())
