from PySide6.QtCore import Qt, QAbstractTableModel

class RebarTableModel(QAbstractTableModel):
    def __init__(self, rebar_dict=None):
        super().__init__()
        self._rebar_dict = rebar_dict or {}
        self._keys = list(self._rebar_dict.keys())  # Store the keys to keep order
        self._headers = ["Name", "Diameter", "Area", "Fy", "Es"]

    def rowCount(self, parent=None):
        return len(self._rebar_dict)

    def columnCount(self, parent=None):
        return 5  # name, diameter, area, Fy, Es

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            key = self._keys[index.row()]
            rebar = self._rebar_dict[key]
            col = index.column()
            if col == 0:
                return rebar.name
            elif col == 1:
                return rebar.diameter
            elif col == 2:
                return rebar.area
            elif col == 3:
                return rebar.Fy
            elif col == 4:
                return rebar.Es

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            else:
                return str(section + 1)
        return None

