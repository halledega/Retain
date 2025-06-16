from enum import Enum
from abc import ABC, abstractmethod
import uuid
from Classes.Wall import Wall

class LoadCategory(Enum):
    DEAD = 1
    LIVE = 2
    STORAGE_LIVE = 3
    SNOW = 4
    SEISMIC = 5
    SOIL = 6
    COMPACTION = 7

class LoadType(Enum):
    HYDROSTATIC = 1
    COMPACTION = 2
    SURCHARGE = 3
    WALL = 4
    SEISMIC = 5

class Load(ABC):
    def __init__(self, name: str, load_type: LoadType, category: LoadCategory, value: float) -> None:
        self.id = str(uuid.uuid4())  # Unique identifier
        self.name = name
        self.category = category
        self.load_type = load_type
        self.value = value

    @abstractmethod
    def P(self, wall) -> float:
        pass

    @abstractmethod
    def M(self, wall) -> float:
        pass

    @abstractmethod
    def W(self) -> float:
        pass

    def __repr__(self) -> str:
        return f"Name: {self.name}, Type: {self.load_type.name}, Category: {self.category.name}, Value: {self.value}"

class HydroStaticLoad(Load):
    def P(self, wall: Wall) -> float:
        h = (wall.height + wall.toe_cover + wall.footing_thickness) / 1000
        p = self.value * h / 2
        return p

    def M(self, wall: Wall) -> float:
        h = (wall.height + wall.toe_cover + wall.footing_thickness) / 1000
        x = h / 3
        p = self.value * h / 2
        m = p * x
        return m

    def W(self, wall: Wall) -> float:
        w = self.value * wall.heel_length * wall.height
        return w

class SurchargeLoad(Load):
    def P(self, wall: Wall) -> float:
        p = self.value * wall.height
        return p

    def M(self, wall: Wall) -> float:
        x = wall.height/2000
        m = self.value * x
        return m

    def W(self, wall: Wall) -> float:
        w = self.value * (wall.height/1000) * (wall.heel_length/1000)
        return w

class WallLoad(Load):
    def P(self, wall: Wall) -> float:
        p = self.value
        return p

    def M(self, wall: Wall) -> float:
        x = (wall.toe_length + wall.thickness/2)/1000
        m = self.value * x
        return m

    def W(self, wall: Wall) -> float:
        return self.P(wall)

class CompactionLoad(Load):
    def P(self, wall: Wall) -> float:
        p = self.value * wall.height
        return p

    def M(self, wall: Wall) -> float:
        x = wall.height/2
        m = self.value * x
        return m

    def W(self) -> float:
        return 0.0

class SeismicLoad(Load):
    def P(self, wall: Wall) -> float:
        pass

    def M(self, wall: Wall) -> float:
        pass

    def W(self) -> float:
        return 0.0