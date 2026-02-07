import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QComboBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ciphy")
        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        # Create a central widget and set the layout
        central_widget = QWidget()
        self.layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        
        # Title Label
        self.label = QLabel("Ciphy")
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )
        
        # Set the font to Menlo, size 30, and bold style
        font = QFont("Menlo", 30, QFont.Weight.Bold)  
        self.label.setFont(font)
        # Set the text color to pastel pink
        self.label.setStyleSheet("color: #FFC5D3;")  
        self.layout.addWidget(self.label)

        #Dropdown menu
        self.label_dropdown = QLabel("Select Cipher:")
        self.layout.addWidget(self.label_dropdown)
        self.dropdown_menu = QComboBox()
        self.dropdown_menu.addItems(["Caesar", "Vigenère", "Permutation"])
        self.layout.addWidget(self.dropdown_menu)
        # Button
        self.button = QPushButton("Encrypt")
        self.layout.addWidget(self.button)

    def _connect_signals(self):
        # Connect button click to a method
        self.button.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        # Placeholder for button click action
        print("Caesar button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec())