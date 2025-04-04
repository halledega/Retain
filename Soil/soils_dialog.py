# Import system
import sys
# PySide6 Imports
from PySide6 import QtCore as Qtc
from PySide6 import QtWidgets as Qtw
# Custom Imports
from Soil.UI.soils_dialog import Ui_dl_soils
#from Database.db_functions import *
from Classes.Soil import Soil

class SoilsDialog(Qtw.QDialog, Ui_dl_soils):
    # Signals
    soil_updated = Qtc.Signal(list)
    def __init__(self, soil):
        super().__init__()
        # Run setup method of UI file
        # This sets up and UI that was created in the UI file
        self.setupUi(self)
        # Get the object that called in window (should be MainWindow)
        #self.caller = main_window
        # Connect line edit signals to slot
        self.le_name.textChanged.connect(self.check_type_string)
        # Connect to Widgets
        # Ok Button
        self.pb_OK.clicked.connect(self.update_soil)
        # Cancel Button
        self.pb_Cancel.clicked.connect(self.close)
        # Set initial values
        self.soil = soil
        self.populate_data()
        # Show Widget
        self.show()

    def populate_data(self):
        self.le_name.setText(self.soil.name)
        self.le_unitWeight.setText(str(self.soil.unit_weight))
        self.le_ulsBearing.setText(str(self.soil.uls_bearing))
        self.le_slsBearing.setText(str(self.soil.sls_bearing))
        self.le_frictionCoeff.setText(str(self.soil.friction_coeff))
        self.le_activeCoeff.setText(str(self.soil.active_coeff))
        self.le_passiveCoeff.setText(str(self.soil.passive_coeff))

    @Qtc.Slot(list)
    def update_soil(self):
        soil_ppts = [
            self.le_name.text().strip(),
            float(self.le_unitWeight.text().strip()),
            float(self.le_ulsBearing.text().strip()),
            float(self.le_slsBearing.text().strip()),
            float(self.le_frictionCoeff.text().strip()),
            float(self.le_activeCoeff.text().strip()),
            float(self.le_passiveCoeff.text().strip()),
        ]

        self.soil_updated.emit(soil_ppts)

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
    test_soil = Soil("test", 20, 300, 200, 0.3, 0.3, 3)
    window = SoilsDialog(Qtw.QMainWindow)
    # Handle application shutdown
    sys.exit(app.exec())