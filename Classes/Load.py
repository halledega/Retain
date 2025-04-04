from enum import Enum 

class Load_Category(Enum):
    DEAD = 1
    LIVE = 2
    STORGAE_LIVE = 3
    SNOW = 4
    SOIL = 5
    COMPACTION = 6

class Load_Type(Enum):
    HYDOSTATIC = 1
    COMPACTION = 2
    SURCHARGE = 3
    WALL = 4

class Load():
    def __init__(self, load_type: Load_Type, category: Load_Category, name: str, value: float) -> None:
        self.Name = name
        self.Category = category
        self.Type = load_type
        self.Value = value

class Wall():
    def __init__(self, name: str, height: float, wall_thickness: float, toe_length: float, footing_length: float, heel_length: float, concrete: Concrete) -> None:
        self.Name = name
        self.Height = height
        self.Wall_Thickness = wall_thickness
        self.Toe_length = toe_length
        self.Footing_Width = footing_width
        self.Heel_Length = heel_length

    self.Concrete: Concrete
    
    self.Loads = {}

    def Add_Load(load_type: Load_type, category: Load_Castegory, name: str, value:float) -> None:
        self.Loads[name] = Load(name, category, load_type, value)
        
    