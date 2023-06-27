from engine.base.point_mass import PointMass
import numpy as np
import pygame

class Run:
    def __init__(self, full_screen):
        self.full_screen = full_screen
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

    def draw_pt(self, x):
        blue = (0, 0, 255)
        radius = 5
        position = self.to_pygame([x.p[0], x.p[1]])
        pygame.draw.circle(self.screen, blue, position, radius)

    def draw_pts(self):
        for x in self.pts:
            self.draw_pt(x)

    def initialize_pts(self):
        x = PointMass(np.array([200, 600]), np.array([20, 0]), np.array([0, 0]), 1, -6)
        self.pts.append(x)

    def update_frame(self):
        for pt in self.pts:
            self.draw_pt(self.pts[0])
            dt = 0.2
            pt.step(dt)

    def run(self):

        self.initialize_pts()

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
            # pygame.time.delay(200)
            pygame.time.Clock().tick(60)

            # Update the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()