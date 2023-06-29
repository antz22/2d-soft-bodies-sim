from engine.base.point_mass import PointMass
from engine.bodies.solid import Solid
from engine.bodies.polygon import Polygon
import numpy as np
import pygame

class Run:
    def __init__(self, full_screen):
        self.full_screen = full_screen
        self.solids = []
        self.polygons = []
        self.pts = []

        pygame.init()

        # Set up the drawing window
        if self.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode([1200, 700])

    def to_pygame(self, x):
        """Convert coordinates into pygame coordinates (lower-left => top left)."""
        height = self.screen.get_height()
        return (x[0], height - x[1])

    def draw_pt(self, pt):
        blue = (0, 0, 255)
        radius = 5
        position = self.to_pygame([pt.p[0], pt.p[1]])
        pygame.draw.circle(self.screen, blue, position, radius)

    def draw_polygon(self, polygon):
        blue = (0, 0, 255)

        for i in range(len(polygon.pts)-1):
            A = polygon.pts[i]
            B = polygon.pts[i+1]
            pygame.draw.line(self.screen, blue, A, B)
        pygame.draw.line(self.screen, blue, polygon.pts[len(polygon.pts)-1], polygon.pts[0])
            
    def draw_spring(self, spring):
        red = (255, 0, 0)
        A = self.to_pygame(spring.A.p)
        B = self.to_pygame(spring.B.p)
        pygame.draw.line(self.screen, red, A, B)

    def init_pts(self):

        p = np.array([200.0, 100.0])
        v = np.array([0.0, 0.0])
        a = np.array([0.0, 0.0])
        m = 1
        g = -6

        pts = [
            PointMass(p=p, v=v, a=a, m=m, g=g)
        ]

        self.pts = pts

    def init_polygons(self):

        pts = np.array([
            [100.0, 20.0],
            [110.0, 40.0],
            [140.0, 60.0],
            [180.0, 70.0],
        ])

        self.polygons.append(Polygon(pts=pts))
        
    def init_solids(self):

        p = np.array([400.0, 600.0])
        v = np.array([0.0, 0.0])
        a = np.array([0.0, 0.0])
        m = 1
        g = -6

        step = 30.0

        m = 8
        n = 8

        pts = []

        for i in range(m):
            pts.append([])
            for j in range(n):
                pts[i].append(PointMass(p + np.array([i*step, j*step]), v, a, m, g))

        s = Solid(m=m, n=n, pts=pts)
        self.solids.append(s)

    def update_frame(self):
        dt = 0.05
        for solid in self.solids:
            for spring in solid.springs:
                self.draw_spring(spring)
            for row in solid.pts:
                for pt in row:
                    self.draw_pt(pt)
                    pt.step(dt)

        for polygon in self.polygons:
            self.draw_polygon(polygon)

        for pt in self.pts:
            self.draw_pt(pt)
            pt.step(dt)
        


    def run(self):

        self.init_solids()
        self.init_polygons()
        self.init_pts()

        # Run until the user asks to quit
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            self.update_frame()
            pygame.time.Clock().tick(60)

            # Update the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()