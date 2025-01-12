import sys
from PySide6.QtWidgets import QApplication

from classes.MainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow('Retain', 1500, 800)
window.show()

app.exec()