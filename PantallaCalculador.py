# PantallaCalculadora.py
if __name__ == "__main__":
from model import Model
from view import View
from presenter import Presenter
app = QtWidgets.QApplication(sys.argv)
# Instanciamos los objetos de forma independiente
modelo = Model()
vista = View()
# El Presenter los une mediante AGREGACIÓN
presentador = Presenter(vista, modelo)
vista.show()
sys.exit(app.exec_())