class Soil():
    def __init__(self, name, unit_weight, uls_earing, sls_bearing, friction_coeff, active_coeff, passive_coeff):
        self.name = name
        self.unit_weight = unit_weight
        self.uls_bearing = uls_earing
        self.sls_bearing = sls_bearing
        self.friction_coeff = friction_coeff
        self.active_coeff = active_coeff
        self.passive_coeff = passive_coeff