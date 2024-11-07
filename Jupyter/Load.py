from enum import Enum

class Load_Category(Enum):
    DEAD = 1
    LIVE = 2
    STORAGE_LIVE = 3
    SNOW = 4
    SEISMIC = 5
    SOIL = 6
    COMPACTION = 7

class Load_Type(Enum):
    HYDROSTATIC = 1
    SURCHARGE = 2
    WALL = 3
    SEISMIC = 4

class Load():
    def __init__(self, load_type: Load_Type, category: Load_Category, name: str, value: float) -> None:
        self.Name = name
        self.Category = category
        self.Type = load_type
        self.Value = value
        
class Concrete():
    def __init__(self, name: str, fc: float, density: str = 'normal'):
        self.Name = name
        self.fc = fc
        self.Denesity = density
        self.Unit_Weight = 24
        
class Soil():
    def __init__(self, name: str, density: float, ka: float, ko: float, kp: float, q_uls: float, q_sls: float, mu: float):
        self.Name = name
        self.Density = density
        self.ka = ka
        self.ko = ko
        self.kp = kp
        self.Q_uls = q_uls
        self.Q_sls = q_sls
        self.Mu = mu

class Wall():
    def __init__(self, name: str, height: float, wall_thickness: float, toe_length: float, footing_length: float, footing_thickness: float, heel_length: float, concrete: Concrete) -> None:
        self.Name = name
        self.Height = height
        self.Wall_Thickness = wall_thickness
        self.Toe_length = toe_length
        self.Footing_Length = footing_length
        self.Heel_Length = heel_length
        self.Footing_Thickness = footing_thickness

        self.Concrete: Concrete
    
        self.Loads = {}

    def Add_Load(self, load_type: Load_Type, category: Load_Category, name: str, value:float) -> None:
        self.Loads[name] = Load(load_type, category, name, value)
        
    