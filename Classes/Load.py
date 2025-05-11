from enum import Enum
from abc import ABC, abstractmethod

from Classes.Wall import Wall


class Load_Category(Enum):
    DEAD = 1
    LIVE = 2
    STORGAE_LIVE = 3
    SNOW = 4
    SEISMIC = 5
    SOIL = 6
    COMPACTION = 7

class Load_Type(Enum):
    HYDOSTATIC = 1
    COMPACTION = 2
    SURCHARGE = 3
    WALL = 4
    SEISMIC = 5

class Load(ABC):
    def __init__(self, load_type: Load_Type, category: Load_Category, name: str, value: float) -> None:
        self.name = name
        self.category = category
        self.Load_type = load_type
        self.value = value

    @abstractmethod
    def P(self, wall) -> float:
        pass

    @abstractmethod
    def M(self, wall):
        pass

class HydroStatic(Load):
    def P(self, wall: Wall) -> float:
        h = (wall.height + wall.toe_cover + wall.footing_thickness) / 1000
        p = self.value * h / 2
        return p

    def M(self, wall: Wall) -> float:
        h = (wall.height + wall.toe_cover + wall.footing_thickness) / 1000
        x = h / 2
        p = self.value * h / 2
        m = p * x
        return m

    def W(self, wall: Wall) -> float:
        w = self.value * wall.heel_length * wall.height
        return w

class Surcharge(Load):
    def P(self, wall: Wall) -> float:
        pass

    def M(self, wall: Wall) -> float:
        pass

class Wall(Load):
    def P(self, wall: Wall) -> float:
        pass

    def M(self, wall: Wall) -> float:
        pass

class Compaction(Load):
    def P(self, wall: Wall) -> float:
        pass

    def M(self, wall: Wall) -> float:
        pass

class Seismic(Load):
    def P(self, wall: Wall) -> float:
        pass

    def M(self, wall: Wall) -> float:
        pass
