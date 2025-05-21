from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from style import ESTILO_PADRAO  # importar o estilo no topo

class TelaMenu(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.setStyleSheet(ESTILO_PADRAO)  # aplicar o estilo


        layout = QVBoxLayout()

        btn_recado = QPushButton("Abrir Gerador de Recado")
        btn_recado.clicked.connect(self.ir_para_recado)
        layout.addWidget(btn_recado)

        btn_relatorio = QPushButton("Abrir Tela de Relatórios")
        btn_relatorio.clicked.connect(self.ir_para_relatorio)
        layout.addWidget(btn_relatorio)

        self.setLayout(layout)

    def ir_para_recado(self):
        self.controlador.setCurrentIndex(1)

    def ir_para_relatorio(self):
        self.controlador.setCurrentIndex(2)
