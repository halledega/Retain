# PySide6 Imports
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
# Layouts
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
# Cutom Imoports
from tools import Functions

soil_inputs = [
    ("ULS Bearing", "300.0", "kPa"),
    ("SLS Bearing", "300.0", "kPa"),
    ("Active Pressure Coef.", "300.0", "ko"),
    ("Passive Pressure Coef.", "300.0", "kp"),
    ("Friction Coef.", "300.0", None)
]

wall_inputs = [
    ("Height(h)", "1200.0", "mm"),
    ("Toe Cover(tc)", "1200.0", "mm"),
    ("Footing Thickness (D)", "1200.0", "mm"),
    ("Wall Thickness (tw)", "1200.0", "mm"),
    ("Toe Length (toe)", "1200.0", "mm"),
    ("Footing Length (b)", "1200.0", "mm")
]

class LeftBar(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignTop)

        self.addWidget(Header("Soil Properties"))
        for soil_input in soil_inputs:
            self.addWidget(InputRow(*soil_input))

        
        self.addWidget(Header("Wall Properties"))
        for wall_input in wall_inputs:
            self.addWidget(InputRow(*wall_input))

class Header(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setText(text)
        self.setFixedHeight(50)
        self.setStyleSheet("font-size: 20px; font-weight: bold;")

class InputRow(QWidget):
    def __init__(self, label, value, description = None):
        super().__init__()
               
        self.app = QApplication.instance()

        self.label = QLabel(label)
        self.label.setFixedWidth(150)
        self.label.setAlignment(Qt.AlignLeft)
        
        self.value = QLineEdit()
        self.value.setPlaceholderText(value)
        self.value.setText(value)
        self.value.setFixedWidth(100)
        self.value.setAlignment(Qt.AlignLeft)
        self.value.textChanged.connect(Functions.InputChanged)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.value)
        if description:
            layout.addWidget(QLabel(description))
        
        layout.setAlignment(Qt.AlignLeft)
        self.setLayout(layout)

    def InputChanged(self, text):
        if text is None:
            pass    
        else:
            print(text)