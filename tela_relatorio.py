from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from style import ESTILO_PADRAO

class TelaRelatorio(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.setStyleSheet(ESTILO_PADRAO)


        layout = QVBoxLayout()
        layout.addWidget(QLabel("📊 Relatórios em construção..."))

        btn_voltar = QPushButton("🔙 Voltar ao Menu")
        btn_voltar.clicked.connect(self.voltar_menu)
        layout.addWidget(btn_voltar)

        self.setLayout(layout)

    def voltar_menu(self):
        self.controlador.setCurrentIndex(0)
