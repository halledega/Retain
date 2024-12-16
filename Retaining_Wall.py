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
    COMPACTION = 3
    WALL = 4
    SEISMIC = 5

class Load():
    def __init__(self, load_type: Load_Type, category: Load_Category, name: str, value: float) -> None:
        self.Name = name
        self.Category = category
        self.Type = load_type
        self.Value = value
        
class Concrete:
    def __init__(self, name: str, density: str = 'normal'):
        self._name = name
        self._fc = 25
        self.phi = 0.65
        self._density = density

        # Initialize dependent properties
        self.update_dependent_properties()

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, value: str) -> None:
        parts = value.split('C')
        if len(parts) == 2 and parts[1].isdigit():
            self.fc = float(parts[1])  # Set fc, which also updates dependent properties
            self._name = value
        else:
            raise ValueError("Invalid concrete name format. Use 'CXX' format.")

    @property
    def fc(self) -> float:
        return self._fc

    @fc.setter
    def fc(self, value: float) -> None:
        self._fc = value
        self.update_dependent_properties()

    @property
    def Density(self) -> str:
        return self._density

    @Density.setter
    def Density(self, value: str) -> None:
        if value not in ['normal', 'lightweight']:
            raise ValueError("Density must be 'normal' or 'lightweight'.")
        self._density = value
        self.lamb = 1.0 if self._density == 'normal' else 0.85

    @property
    def alpha1(self) -> float:
        return self._alpha1

    @property
    def beta1(self) -> float:
        return self._beta1

    def update_dependent_properties(self):
        """
        Updates dependent properties based on fc.
        """
        self._alpha1 = max(0.67, 0.85 - 0.0015 * self.fc)
        self._beta1 = max(0.67, 0.97 - 0.0025 * self.fc)
       
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
    def __init__(self, name: str, height: float, wall_thickness: float, toe_cover: float, toe_length: float, footing_length: float, footing_thickness: float) -> None:
        self.Name = name
        self.Height = height
        self.Wall_Thickness = wall_thickness
        self.Toe_Cover = toe_cover
        self.Toe_Length = toe_length
        self.Footing_Length = footing_length
        self.Footing_Thickness = footing_thickness
        self._heel_length = 0
  
        self.Loads = {}

    @property 
    def Heel_Length(self) -> float:
        return self._heel_length
    @Heel_Length.setter
    def Heel_Length(self):
        self._heel_length = self.Footing_Length - self.Toe_Length - self.Wall_Thickness


    def Add_Load(self, load_type: Load_Type, category: Load_Category, name: str, value:float) -> None:
        self.Loads[name] = Load(load_type, category, name, value) 