import numpy as np

class PointMass:
    """
    Class to model a point mass in the simulation.

    p: Position (vector)
    v: Velocity (vector)
    a: Acceleration (vector)
    m: Mass (scalar)
    g: Gravity (scalar)
    """
    def __init__(self, p, v, a, m, g):
        self.p = p
        self.v = v
        self.a = a
        self.m = m
        self.g = g
        self.forces = {"g": np.array([0.0, g])}

    def resetA(self):
        # self.a[0] = 0.0
        # self.a[1] = self.g
        pass

    def applyForces(self):
        self.a = np.array([0.0, 0.0])
        for F in self.forces:
            self.a += self.forces[F] / self.m

    # def reflectV(self, v):
        # if np.linalg.norm(v) != 0:
        #     v *= 0.995 / np.linalg.norm(v)
        # self.v -= 2 * np.dot(self.v, v) * v

    def step(self, dt):
        self.applyForces()
        self.p[0] += self.v[0]*dt
        self.p[1] += self.v[1]*dt
        self.v[0] += self.a[0]*dt
        self.v[1] += self.a[1]*dt
        if self.p[1] <= 0.0:
            self.p[1] = 0.0
            self.v[1] *= -0.85
            # self.reflectV(np.array([0, 1.0]))