class Concrete:
    def __init__(self, name, fc, unit_weight, density):
        self.name = name
        self.fc = fc
        self.unit_weight = unit_weight
        self.density = density
        self._alpha1 = 0
        self._beta1 = 0
        self._ec = 0
        self._lambda = 0

    @property
    def alpha1(self):
        self._alpha1 = round(max(0.67, 0.85-self.fc*0.0015),3)
        return self._alpha1

    @property
    def beta1(self):
        self._beta1 = round(max(0.67, 0.97-self.fc * 0.0025),3)
        return self._beta1

    @property
    def ec(self):
        self._ec = round(4500 * self.fc ** 0.5,0)
        return self._ec

    @property
    def lamb(self):
        if self.density.lower() == "normal" :
            self._lambda = 1.0
        else:
            self._lambda = 0.8
        return self._lambda

