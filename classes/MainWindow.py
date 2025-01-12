#Pyside6 imports
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QComboBox, QRadioButton, QInputDialog, QLabel, QMenuBar, QStatusBar, QTabBar, QToolBar, QLineEdit
# 
from PySide6.QtCore import Qt, QSize
# layouts
from PySide6.QtWidgets import QLayout, QVBoxLayout, QHBoxLayout, QGridLayout 
from PySide6.QtGui import QPalette, QColor

#
from classes import LeftBar, Canvas

class Menu_Bar(QMenuBar):
    def __init__(self):
        super().__init__()
        
        self.file = self.addMenu('File')
        self.edit = self.addMenu('Edit')
        self.help = self.addMenu('Help')

        self.file.addMenu('New')
        self.file.addMenu('Open')
        self.file.addMenu('Save')
        self.file.addMenu('Save As')

        self.help.addMenu('About')

class Tool_Bar(QToolBar):
    def __init__(self):
        super().__init__()

class Status_Bar(QStatusBar):
    def __init__(self):
        super().__init__()

class MainWindow(QMainWindow):
    def __init__(self, window_title, width, height):
        
        super().__init__()

        self.setWindowTitle(window_title)
        self.setMinimumSize(width, height)

        menu_bar = Menu_Bar()
        tool_bar = Tool_Bar()
        status_bar = Status_Bar()

        main_layout = QHBoxLayout()
        
        left_bar = LeftBar.LeftBar()

        canvas = Canvas.Canvas()
        right_bar = QVBoxLayout()

        main_layout.addLayout(left_bar, 0)
        main_layout.addLayout(canvas, 3)
        main_layout.addLayout(right_bar, 1)

        primary_widget = QWidget()
        primary_widget.setLayout(main_layout)

        self.setMenuBar(menu_bar)
        self.addToolBar(tool_bar)
        self.setCentralWidget(primary_widget)
        self.setStatusBar(status_bar)