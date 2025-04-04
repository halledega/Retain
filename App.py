# Import system
import sys
# Python Imports
# PySide6 Imports
from PySide6 import QtCore as Qtc
from PySide6 import QtWidgets as Qtw
#from PySide6 import QtGui as QtGui
# UI Imports
from Main.UI.main_window import Ui_mw_MainWindow
from Soil.soils_dialog import SoilsDialog
from Materials.materials_dialog import MaterialsDialog
#from Application_Login.login import LoginForm
#Custom Imports
from Database.db_functions import *
from Classes.Soil import Soil
from Classes.Concrete import Concrete

class MainWindow(Qtw.QMainWindow, Ui_mw_MainWindow):
    def __init__(self):
        super().__init__()
        # Placeholder properties, forms and dialogs
        self.form = None
        self.soil = None
        self.concrete = None
        # Run Newfile method
        self.start_up()
        # Run setup method of UI file
        # This sets up and UI that was created in the UI file
        self.setupUi(self)
        # Define -> Soil action
        self.a_defineSoil.triggered.connect(self.open_soils_dialog)
        self.a_defineMaterials.triggered.connect(self.open_materials_dialog)
        # File -> Close Actions
        self.a_exit.triggered.connect(self.close)
        # Show MainWindow
        self.show()

    @Qtc.Slot()
    def open_soils_dialog(self):
        self.form = SoilsDialog(self.soil)
        self.form.soil_updated.connect(self.update_soil)
        self.form.show()

    @Qtc.Slot()
    def open_materials_dialog(self):
        self.form = MaterialsDialog(self.concrete)
        self.form.materials_updated.connect(self.update_materials)
        self.form.show()

    @Qtc.Slot(str)
    def update_soil(self, my_str):
        self.soil.name = my_str[0]
        self.soil.unit_weight = my_str[1]
        self.soil.uls_bearing = my_str[2]
        self.soil.sls_bearing = my_str[3]
        self.soil.friction_coeff = my_str[4]
        self.soil.active_coeff = my_str[5]
        self.soil.passive_coeff = my_str[6]

    @Qtc.Slot(str)
    def update_materials(self, my_str):
        # self.soil.name = my_str[0]
        # self.soil.unit_weight = my_str[1]
        # self.soil.uls_bearing = my_str[2]
        # self.soil.sls_bearing = my_str[3]
        # self.soil.friction_coeff = my_str[4]
        # self.soil.active_coeff = my_str[5]
        # self.soil.passive_coeff = my_str[6]
        pass

    def start_up(self):
        # Connect to settings DB
        settings_db = sql_connect('retain.db')
        # Get defaults and add to file db
        default_soil = return_data(settings_db['Connection'], settings_db['Cursor'], 'Soil')[0]
        default_concrete = return_data(settings_db['Connection'], settings_db['Cursor'], 'Concrete')[0]
        # Create Soil object
        self.soil = Soil(default_soil[1], default_soil[2], default_soil[3], default_soil[4], default_soil[5], default_soil[6], default_soil[7])
        self.concrete = Concrete(default_concrete[1], default_concrete[2], default_concrete[3], default_concrete[4])

if __name__ == "__main__":
    # Create new QApplication instance
    app = Qtw.QApplication(sys.argv)
    # Create window object (could also be a widget)
    window = MainWindow()
    # Handle application shutdown
    sys.exit(app.exec())

    # Dictionary of Tables
    # table_names = {
    #     'Concrete': [('Name', 'TEXT'),('Compressive Strength', 'REAL'),('Unit Weight', 'REAL'),('Density','TEXT')],
    #     'Soil': [('Name','TEXT'), ('Unit Weight','REAL'), ('ULS Bearing','REAL'), ('SLS Bearing','REAL'), ('Friction Coefficient','REAL'), ('Active Pressure Coefficient','REAL'), ('Passive Pressure Coefficient','REAL')],
    #     'Rebar': [('Name','TEXT'), ('Diameter','REAL'), ('Area','REAL'), ('Yield Stress','REAL')]
    #     }
    # # Create new db in memory for new file
    # start_up_db = sql_connect()
    # for k, v in table_names.items:
    #     create_table(settings_db['Connection'], settings_db['Cursor'],k, v)
    #     # Loop over column names and create
    #     # Insert default data into tables
    #     insert_data(start_up_db['Connection'], start_up_db['Connection'], k, data_dict)
