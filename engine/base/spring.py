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
        x = np.linalg.norm(self.B.p - self.A.p) - self.L
        dir = (self.B.p - self.A.p) / np.linalg.norm(self.B.p - self.A.p)
        Fs = dir * self.k * x
        print("Fs:", Fs)

        # Calculate damping force
        print("Dir:", dir)
        v = self.B.v - self.A.v
        print("V:", v)
        Fd = dir * np.dot(dir, v) * self.d
        print("Fd:", Fd)

        Ft = -Fd + Fs

        self.A.forces[self] = Ft
        self.B.forces[self] = -Ft
        # self.A.applyForce(Ft)
        # self.B.applyForce(-Ft)


        # # Calculate spring force
        # x = np.linalg.norm(self.A.p - self.B.p) - self.L
        # dir = (self.A.p - self.B.p) / np.linalg.norm(self.A.p - self.B.p)
        # Fs = self.k * x
        # print("Fs:", Fs)

        # # Calculate damping force
        # print("Dir:", dir)
        # v = self.B.v - self.A.v
        # print("V:", v)
        # Fd = np.dot(v, dir) * self.d
        # print("Fd:", Fd)

        # Ft = dir * (-Fd + Fs)

        # self.A.applyForce(Ft)
        # self.B.applyForce(-Ft)

        # unit = ((self.A.p - self.B.p) / np.linalg.norm(self.A.p - self.B.p))
        # proj_v = np.dot((self.B.v - self.A.v), unit)
        # self.B.applyForce(((-self.k * (np.linalg.norm(self.A.p - self.B.p) - self.L)) + (proj_v*self.d)) * (-1 * unit))
        # self.A.applyForce(((-self.k * (np.linalg.norm(self.A.p - self.B.p) - self.L)) + (proj_v*self.d)) * (unit))