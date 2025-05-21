import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget

from tela_menu import TelaMenu
from tela_recado import RecadoApp
from tela_relatorio import TelaRelatorio
from style import ESTILO_PADRAO

class Controlador(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(ESTILO_PADRAO)  # aplicar o estilo

        # Instanciar telas
        self.tela_menu = TelaMenu(self)
        self.tela_recado = RecadoApp(self)
        self.tela_relatorio = TelaRelatorio(self)


        # Adicionar ao QStackedWidget
        self.addWidget(self.tela_menu)      # index 0
        self.addWidget(self.tela_recado)    # index 1
        self.addWidget(self.tela_relatorio) # index 2

        self.setWindowTitle("Sistema de Recados")
        self.setFixedSize(800, 700)
        self.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlador = Controlador()
    controlador.show()
    sys.exit(app.exec_())
