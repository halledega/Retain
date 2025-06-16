# Import system
import sys
# PySide6 imports
from PySide6 import QtCore as Qtc
from PySide6 import QtWidgets as Qtw
#Custom imports
from Loads.UI.loads_dialog import Ui_dl_loads
from Classes.Load import LoadCategory, LoadType#, HydroStaticLoad, SurchargeLoad, WallLoad, CompactionLoad, SeismicLoad
from Classes.LoadManager import LoadManager

class LoadsDialog(Qtw.QDialog, Ui_dl_loads):
    # Signals
    lb_item_clicked = Qtc.Signal(object)
    def __init__(self, load_manager: LoadManager, load_type: LoadType) -> None:
        super().__init__()
        # Run setup method of UI file
        # This sets up and UI that was created in the UI file
        self.setupUi(self)
        # Connect line edit signals to slot
        self.le_name.textChanged.connect(self.check_type_string)
        # Connect to Widgets
        # Ok Button
        self.pb_OK.clicked.connect(self.close)
        # Cancel Button
        self.pb_Cancel.clicked.connect(self.close)
        # Listbox
        self.lb_loads.itemClicked.connect(self.get_selected_item)
        # New Button
        self.pb_new.clicked.connect(self.new_load)
        # Save Button
        self.pb_save.clicked.connect(self.save_load)
        # Set initial values
        self.load_manager = load_manager
        self.load_type = load_type
        self.load = None # Placeholder for selected load used to edit and save etc.
        self.populate_combo_boxes()
        self.populate_list_box()
        # Show Widget
        self.show()

    def populate_combo_boxes(self):
        for category in LoadCategory:
            self.cb_category.addItem(category.name, category)
        for load_type in LoadType:
            self.cb_type.addItem(load_type.name, load_type)

    def populate_list_box(self):
        self.lb_loads.clear()
        for load in self.load_manager.get_loads():
            if load.load_type == self.load_type:
                item = Qtw.QListWidgetItem(load.name)
                item.setData(Qtc.Qt.ItemDataRole.UserRole, load)
                self.lb_loads.addItem(item)

    @Qtc.Slot()
    def check_type_string(self, text):
        if type(text) == str:
            pass

    @Qtc.Slot()
    def get_selected_item(self):
        selected_item = self.lb_loads.currentItem()
        if selected_item:
            self.load = selected_item.data(Qtc.Qt.ItemDataRole.UserRole)
            self.le_name.setText(self.load.name)
            self.le_value.setText(str(self.load.value).strip())
            self.cb_category.setCurrentText(self.load.category.name)
            self.cb_type.setCurrentText(self.load.load_type.name)

    @Qtc.Slot()
    def new_load(self):
        self.le_name.setText('New Load')
        self.le_value.setText(str(0.0))
        self.cb_category.setCurrentText('SOIL')
        self.cb_type.setCurrentText(self.load_type.name)


    @Qtc.Slot()
    def save_load(self):
        self.load.name = self.le_name.text()
        self.load.value = float(self.le_value.text().strip())
        self.load.category = self.cb_category.currentData()
        self.load.load_type = self.cb_type.currentData()
        self.populate_list_box()
        print(self.load)
