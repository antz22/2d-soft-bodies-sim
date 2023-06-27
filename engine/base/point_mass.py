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
        self.a[1] = g

    def getP(self):
        return (self.p[0], self.p[1])

    def updateP(self, dp):
        self.p[0] += dp[0]
        self.p[1] += dp[1]

    def applyF(self, F):
        self.a[0] += F[0]/self.m
        self.a[1] += F[1]/self.m

    def step(self, dt):
        self.p[0] += self.v[0]*dt
        self.p[1] += self.v[1]*dt
        self.v[0] += self.a[0]*dt
        self.v[1] += self.a[1]*dt
        if self.p[1] <= 0:
            self.p[1] = 0
            self.a[1] = 0



    
    
        