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
    
    def calcForces(self):
        # Calculate spring force
        x = (self.B.p - self.A.p) - self.L
        Fs = self.k * x
        self.A.applyForce(Fs)
        self.B.applyForce(-Fs)

        # Calculate damping force
        dir = (self.B.p - self.A.p) / np.linalg.norm(self.B.p - self.A.p)
        v = self.B.v - self.A.v
        Fd = np.dot(dir, v) * self.d
        self.A.applyForce(Fd)
        self.B.applyForce(-Fd)
