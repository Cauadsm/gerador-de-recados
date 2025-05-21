# estilos.py
ESTILO_PADRAO = """
QWidget {
    background-color: #ffe3a1;
    font-family: 'Segoe UI';
    font-size: 11pt;
    color: #333;
}

QLabel {
    font-weight: bold;
    color: #1976D2;
}

QLineEdit, QTextEdit, QComboBox {
    padding: 9px;
    border: 1px solid #1976D2;
    border-radius: 6px;
    background-color: #f9f9f9;
    color: #333;
}

QPushButton {
    background-color: #F57C00;
    color: white;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 8px;
    border: none;
}

QPushButton:hover {
    background-color: #EF6C00;
}

QTextEdit[readOnly="true"] {
    background-color: #f9f9f9;
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
    border-radius: 10px;
}
"""
