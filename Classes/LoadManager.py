from Classes.Load import *

class LoadManager:
    def __init__(self):
        self.loads = []

    def add_load(self, load: Load) -> str:
        self.loads.append(load)
        return load.id  # Return the ID so you can track it

    def delete_load(self, load_id: str) -> bool:
        for i, load in enumerate(self.loads):
            if load.id == load_id:
                del self.loads[i]
                return True
        return False

    def edit_load(self, load_id: str, *, new_name=None, new_type=None, new_category=None, new_value=None) -> bool:
        for load in self.loads:
            if load.id == load_id:
                if new_name:
                    load.name = new_name
                if new_type:
                    load.load_type = new_type
                if new_category:
                    load.category = new_category
                if new_value is not None:
                    load.value = new_value
                return True
        return False

    def get_loads(self) -> list:
        return self.loads
