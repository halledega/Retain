# Import system
import sys
# PySide6 Imports
from PySide6 import QtCore as Qtc
from PySide6 import QtWidgets as Qtw
from PySide6.QtCore import Signal

from Database.db_functions import return_data
# Custom Imports
from Materials.UI.materials_dialog import Ui_dl_materials
#from Database.db_functions import *
from Classes.Concrete import Concrete
#Models
from Models.Rebar_Model import RebarTableModel

class MaterialsDialog(Qtw.QDialog, Ui_dl_materials):
    # Signals
    materials_updated = Qtc.Signal(list)
    rebar_updated = Qtc.Signal(list)
    def __init__(self, concrete, rebar_dict, rebar_settings):
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
        self.populate_data(concrete, rebar_dict, rebar_settings)
        # Show Widget
        self.show()

    def populate_data(self, concrete, rebar_dict, rebar_settings):
        self.le_name.setText(concrete.name)
        self.le_fc.setText(str(concrete.fc))
        self.le_unit_weight.setText(str(concrete.unit_weight))
        self.le_desnity.setText(str(concrete.density))
        self.le_alpha1.setText(str(concrete.alpha1))
        self.le_beta1.setText(str(concrete.beta1))
        self.le_ec.setText(str(concrete.ec))
        self.le_lambda.setText(str(concrete.lamb))
        # Connect Signals and Slots
        self.le_fc.textChanged.connect(self.update_concrete_properties)
        # Populate Reabr Settings
        self.cb_smallest_bar.addItems(rebar_dict.keys())
        self.cb_smallest_bar.setCurrentText(rebar_settings['smallest_bar'].name)
        self.cb_default_bar.addItems(rebar_dict.keys())
        self.cb_default_bar.setCurrentText(rebar_settings['default_bar'].name)
        self.cb_largest_bar.addItems(rebar_dict.keys())
        self.cb_largest_bar.setCurrentText(rebar_settings['largest_bar'].name)
        self.le_min_spacing.setText(str(rebar_settings['min_spacing']))
        self.le_max_spacing.setText(str(rebar_settings['max_spacing']))
        # Populate Rebar Table
        rebar_model = RebarTableModel(rebar_dict)
        self.tv_rebarSizes.setModel(rebar_model)

    @Qtc.Slot(str)
    def update_concrete_properties(self, text) -> None:
        #print(f"Received text: {text}")
        try:
            fc = float(text)
            #print(f"Parsed fc: {fc}")

            alpha = round(max(0.67, 0.85 - fc * 0.0015), 3)
            beta = round(max(0.67, 0.97 - fc * 0.0025), 3)
            Ec = round(4500 * fc ** 0.5, 0)

            #print(f"alpha: {alpha}, beta: {beta}, Ec: {Ec}")

            self.le_alpha1.setText(str(alpha))
            self.le_beta1.setText(str(beta))
            self.le_ec.setText(str(Ec))
            return None
        except Exception as e:
            #print(f"Exception occurred: {e}")
            return None

    @Qtc.Slot(list, list)
    def update_materials(self):
        concrete_ppts = [
            self.le_name.text().strip(),
            float(self.le_fc.text().strip()),
            float(self.le_unit_weight.text().strip()),
            self.le_desnity.text().strip()
        ]
        self.materials_updated.emit(concrete_ppts)

        rebar_ppts = [
            self.cb_smallest_bar.currentText(),
            self.cb_default_bar.currentText(),
            self.cb_largest_bar.currentText(),
            float(self.le_min_spacing.text().strip()),
            float(self.le_max_spacing.text().strip())
        ]
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
    conc = Concrete("test", 25, 24, "normal")
    window = MaterialsDialog(conc)
    # Handle application shutdown
    sys.exit(app.exec())