import PointMass
import numpy as np
class Spring:
    """
    A, B: Point masses on ends of spring
    L: resting length of spring
    k: stiffness of spring
    d: damping factor of spring
    """
    def __init__(self, A, B, L, k, d):
        self.A = A
        self.B = B 
        self.L = L
        self.k = k
        self.d = d
    
    def stepSpring(self):
        v = self.A - self.B
        x, y = v
        norm = np.linalg.norm(v)
        if norm != 0: 
            x, y = v * (norm - self.L) * self.k / norm, v * (self.L - norm) * self.k / norm
        self.A.applyForce(x)
        self.B.applyForce(y)
        

    