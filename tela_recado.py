from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QComboBox, QLineEdit, QTextEdit, QPushButton, QMessageBox
)
from PyQt5.QtGui import QIcon

from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDate
import sys
from datetime import datetime

class RecadoApp(QWidget):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        
        self.setWindowTitle("📢 Gerador de Recados - Prof. Cauã")
        self.setWindowIcon(QIcon("src/icone.ico"))
        self.setFixedSize(800, 700)
        self.setStyleSheet("""
    QWidget {
        background-color: #ffe3a1;  /* Fundo branco */
        font-family: 'Segoe UI';
        font-size: 11pt;
        color: #333;
    }

    QLabel {
        font-weight: bold;
        color: #1976D2;  /* Azul para rótulos */
    }

    QLineEdit, QTextEdit, QComboBox {
        padding: 9px;
        border: 1px solid #1976D2;  /* Borda azul */
        border-radius: 6px;
        background-color: #f9f9f9;  /* Levemente acinzentado */
        color: #333;
    }

    QPushButton {
        background-color: #F57C00;  /* Laranja */
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
    }

    QPushButton:hover {
        background-color: #EF6C00;  /* Laranja mais escuro ao passar o mouse */
    }

    QTextEdit[readOnly="true"] {
        background-color: #f9f9f9;  /* Azul bem claro para visualização */
        border: 1px solid #90caf9;
    }
    QComboBox::drop-down {
        border: none;
        background-color: #1976D2;
        width: 30px;
        border-top-right-radius: 6px;
        border-bottom-right-radius: 6px;
    }

    QComboBox::down-arrow {
        image: url(src/arrow_down.png);
        width: 16px;
        height: 16px;
    }

    QComboBox QAbstractItemView {
        border: 1px solid #1976D2;
        background-color: #ffffff;
        selection-background-color: #F57C00;
        selection-color: white;
        padding: 6px;
        font-size: 10.5pt;
        border-radius: 10px
    }
    
""")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Título (Professor ou Professora)
        self.titulo_combo = QComboBox()
        self.titulo_combo.addItems(["Professor", "Professora"])
        layout.addLayout(self.linha("Como deseja ser chamado(a):", self.titulo_combo))

        # Nome do professor
        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Ex: Professor Cauã")
        layout.addLayout(self.linha("Seu nome:", self.nome_input))

        # Módulo
        layout.addLayout(self.linha("Módulo:", self.criar_modulo_combo()))

        # Horário
        self.horario_input = QLineEdit()
        self.horario_input.setPlaceholderText("Ex: 14h às 16h")
        layout.addLayout(self.linha("Horário:", self.horario_input))

        # Data
        self.data_input = QLineEdit()
        self.data_input.setInputMask("00/00/0000")  # Máscara para dd-mm-aaaa
        layout.addLayout(self.linha("Data:", self.data_input))

        # Conteúdo
        self.conteudo_input = QTextEdit()
        layout.addLayout(self.linha("Conteúdo da aula:", self.conteudo_input))

        # Link extra
        self.link_input = QLineEdit()
        layout.addLayout(self.linha("Link extra:", self.link_input))

        # Descrição do link
        self.desc_link_input = QTextEdit()
        layout.addLayout(self.linha("Descrição do link:", self.desc_link_input))

        # Botão Gerar
        self.btn_gerar = QPushButton("🚀 Gerar e Copiar Recado")
        self.btn_gerar.clicked.connect(self.gerar_recado)
        layout.addWidget(self.btn_gerar)

        # Botão Limpar
        self.btn_limpar = QPushButton("🧹 Limpar Campos")
        self.btn_limpar.clicked.connect(self.limpar_campos)
        layout.addWidget(self.btn_limpar)

        # Resultado
        self.resultado = QTextEdit()
        self.resultado.setReadOnly(True)
        layout.addWidget(QLabel("Recado Gerado:"))
        layout.addWidget(self.resultado)

        # Botão Voltar
        self.btn_voltar = QPushButton("🔙 Voltar ao Menu")
        self.btn_voltar.clicked.connect(self.voltar_menu)
        layout.addWidget(self.btn_voltar)

        self.setLayout(layout)
        
    def voltar_menu(self):
        self.controlador.setCurrentIndex(0)


    def linha(self, label_texto, widget):
        layout = QHBoxLayout()
        label = QLabel(label_texto)
        label.setFixedWidth(220)
        layout.addWidget(label)
        layout.addWidget(widget)
        return layout

    def criar_modulo_combo(self):
        self.modulo_combo = QComboBox()
        modulos = ["CK 1", "CK 2", "CK 3", "CK4", "CT 1", "CT 2", "CT 3", "CT 4", "CY 1", "CY 2", "CY 3", "CY 4"]
        self.modulo_combo.addItems(modulos)
        return self.modulo_combo

    def gerar_recado(self):
        try:
            titulo = self.titulo_combo.currentText()
            nome = self.nome_input.text().strip() or titulo
            modulo = self.modulo_combo.currentText()
            horario = self.horario_input.text()
            data = self.data_input.text()
            conteudo = self.conteudo_input.toPlainText().strip()
            link = self.link_input.text()
            desc = self.desc_link_input.toPlainText().strip()

            # Ajustar data
            data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")

            # Artigo definido
            artigo = "o" if titulo == "Professor" else "a"

            # Link opcional formatado
            link_bloco = ""
            if link or desc:
                link_bloco = f"\n📎 *Material complementar:* {link}\n"
                if desc:
                    link_bloco += f"_{desc}_"

            # Recado formatado para WhatsApp
            recado = f"""
Olá, pais, mães e responsáveis! Tudo bem?

Aqui é *{artigo} {titulo} {nome}*. Gostaria de compartilhar como foi a aula de hoje com seu(sua) filho(a):

*Módulo:* {modulo}  |  *Horário:* {horario}  |  *Data:* {data_formatada}

📌 *Conteúdo:* {conteudo}

{link_bloco}

Qualquer dúvida, fico à disposição!
""".strip()

            self.resultado.setPlainText(recado)

            # Copiar para área de transferência
            clipboard = QApplication.clipboard()
            clipboard.setText(recado)

            QMessageBox.information(self, "Sucesso!", "Recado gerado e copiado com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro:\n{e}")

    def limpar_campos(self):
        # Limpar todos os campos de entrada
        self.titulo_combo.setCurrentIndex(0)  # Voltar ao valor padrão
        self.nome_input.clear()
        self.modulo_combo.setCurrentIndex(0)
        self.horario_input.clear()
        self.data_input.clear()
        self.conteudo_input.clear()
        self.link_input.clear()
        self.desc_link_input.clear()
        self.resultado.clear()
