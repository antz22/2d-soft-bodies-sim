from ..utils.distance import distance

class Spring:
    """
    A, B: Point masses on ends of spring
    L: resting length of spring
    k_s: stiffness of spring
    k_d: damping factor of spring
    """
    def __init__(self, A, B, L, k_s, k_d):
        self.A = A
        self.B = B 
        self.L = L
        self.k_s = k_s
        self.k_d = k_d

    def calc_displacement(self):
        x = abs(distance(self.A, self.B)) - self.L