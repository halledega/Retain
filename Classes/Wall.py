# PySide6 Imports
from PySide6 import QtCore as Qtc

class Wall:
    def __init__(self, grade_difference, thickness, toe_cover, footing_width, footing_thickness, toe_length):
        self.grade_difference = grade_difference
        self.thickness = thickness
        self.toe_cover = toe_cover
        self.footing_width = footing_width
        self.footing_thickness = footing_thickness
        self.toe_length = toe_length
        self._height = 0
        self._heel_length = 0

    @property
    def height(self):
        self._height = self.grade_difference + self.toe_cover
        return self._height

    @property
    def heel_length(self):
        self._heel_length = self.footing_width - self.toe_length - self.thickness
        return self._heel_length

    def get_wall_rect(self, scaler: float) -> Qtc.QRect:
        wall_x = self.footing_width * scaler - self.toe_length * scaler
        wall_y = -self.height * scaler # draw upwards
        return Qtc.QRect(wall_x, wall_y, self.thickness * scaler, self.height * scaler)

    def get_footing_rect(self, scaler: float) -> Qtc.QRect:
        return Qtc.QRect(0, 0, self.footing_width * scaler, self.footing_thickness * scaler)