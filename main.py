import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

def generate_password():
    try:
        length = int(length_entry.text())
        if length <= 0:
            raise ValueError("La longueur doit être un nombre positif.")
        
        characters = string.ascii_lowercase
        if uppercase_checkbox.isChecked():
            characters += string.ascii_uppercase
        if digits_checkbox.isChecked():
            characters += string.digits
        if special_checkbox.isChecked():
            characters += string.punctuation
        
        if not characters:
            raise ValueError("Aucun caractère sélectionné.")
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.setText(password)
    except ValueError as e:
        QMessageBox.warning(window, "Erreur", str(e))

def copy_to_clipboard():
    clipboard = QApplication.clipboard()
    clipboard.setText(password_entry.text())

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Goupipass")
window.setStyleSheet("""
    background-color: #2e2e2e;
    color: white;
    font-family: Arial;
    font-size: 18px;
""")

window.setWindowIcon(QIcon('oupi goupi.ico'))

layout = QVBoxLayout()

# Champ de longueur du mot de passe
length_layout = QHBoxLayout()
length_label = QLabel("Longueur :")
length_label.setStyleSheet("font-size: 22px; color: white;")
length_entry = QLineEdit()
length_entry.setText("12")
length_entry.setStyleSheet("""
    font-size: 22px;
    padding: 12px;
    background-color: #444444;
    color: white;
    border: none;
    border-radius: 5px;
    width: 120px;
""")
length_layout.addWidget(length_label)
length_layout.addWidget(length_entry)
layout.addLayout(length_layout)

# Cases à cocher
checkbox_layout = QVBoxLayout()
uppercase_checkbox = QCheckBox("Majuscules")
uppercase_checkbox.setStyleSheet("font-size: 20px; color: white;")
digits_checkbox = QCheckBox("Chiffres")
digits_checkbox.setStyleSheet("font-size: 20px; color: white;")
special_checkbox = QCheckBox("Caractères spéciaux")
special_checkbox.setStyleSheet("font-size: 20px; color: white;")

checkbox_layout.addWidget(uppercase_checkbox)
checkbox_layout.addWidget(digits_checkbox)
checkbox_layout.addWidget(special_checkbox)
layout.addLayout(checkbox_layout)

# Bouton de génération
generate_button = QPushButton("Générer")
generate_button.setStyleSheet("""
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 18px;
    border-radius: 5px;
    font-size: 22px;
""")
generate_button.clicked.connect(generate_password)
layout.addWidget(generate_button)

# Champ pour le mot de passe généré
password_entry = QLineEdit()
password_entry.setReadOnly(True)
password_entry.setStyleSheet("""
    background-color: #444444;
    color: white;
    border: none;
    padding: 12px;
    font-size: 22px;
    border-radius: 5px;
""")
layout.addWidget(password_entry)

# Bouton de copie
copy_button = QPushButton("Copier")
copy_button.setStyleSheet("""
    background-color: #2196F3;
    color: white;
    border: none;
    padding: 18px;
    border-radius: 5px;
    font-size: 22px;
""")
copy_button.clicked.connect(copy_to_clipboard)
layout.addWidget(copy_button)

# Fenêtre sans barre de titre
window.setLayout(layout)

# Taille de la fenêtre
window.setGeometry(100, 100, 800, 600)

window.show()

sys.exit(app.exec_())
