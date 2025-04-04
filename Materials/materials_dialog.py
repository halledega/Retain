# Import system
import sys
#from mimetypes import inited
# PySide6 Imports
from PySide6 import QtCore as Qtc
from PySide6 import QtWidgets as Qtw
from PySide6.QtCore import Signal

#from PySide6 import QtGui as qtg
# Custom Imports
from Materials.UI.materials_dialog import Ui_dl_materials
#from Database.db_functions import *


class MaterialsDialog(Qtw.QDialog, Ui_dl_materials):
    # Signals
    materials_updated = Qtc.Signal(list)
    rebar_updated = Qtc.Signal(list)
    def __init__(self, concrete):
        super().__init__()
        # Run setup method of UI file
        # This sets up and UI that was created in the UI file
        self.setupUi(self)
        # Connect line edit signals to slot
        self.le_name.textChanged.connect(self.check_type_string)
        # Connect to Widgets
        # Ok Button
        self.pb_OK.clicked.connect(self.update_materials)
        # Cancel Button
        self.pb_Cancel.clicked.connect(self.close)
        # Set initial values
        self.populate_data(concrete)
        # Show Widget
        self.show()

    def populate_data(self, concrete):
        self.le_name.setText(concrete.name)
        self.le_fc.setText(str(concrete.fc))
        self.le_unit_weight.setText(str(concrete.unit_weight))
        self.le_desnity.setText(str(concrete.density))
        self.le_alpha1.setText(str(concrete.alpha1))
        self.le_beta1.setText(str(concrete.beta1))
        self.le_ec.setText(str(concrete.ec))
        self.le_lambda.setText(str(concrete.lamb))

    @Qtc.Slot(list)
    def update_materials(self):
        concrete_ppts = []
        self.materials_updated.emit(concrete_ppts)

        rebar_ppts = []
        self.rebar_updated.emit(rebar_ppts)

        self.close()

    @Qtc.Slot()
    def check_type_string(self, text):
        if type(text) == str:
            pass

    @Qtc.Slot()
    def display_hint(self):
        sender = self.sender()
        if sender == sender.le_name:
            print("Name of the soil type.")

if __name__ == "__main__":
    # Create new QApplication instance
    app = Qtw.QApplication(sys.argv)
    # Create window object (could also be a widget)
    window = SoilsDialog(Qtw.QMainWindow)
    # Handle application shutdown
    sys.exit(app.exec())