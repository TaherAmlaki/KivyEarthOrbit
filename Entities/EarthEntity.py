from Entities.BaseEntity import Entity
from Paths import ForceAppPath
import numpy as np


class Earth(Entity):
    IMAGE = ForceAppPath.EARTH_IMAGE.path

    def __init__(self, x=None, y=None, size=None):
        super().__init__(x, y, size)
        self._at_inf = False
        self.xc = self.size[0] * 0.5
        self.yc = self.size[1] * 0.5
        self.r = None

    def move(self, *args, **kwargs):
        dt = kwargs.get('dt')
        fvec, fr = self.calculate_force(kwargs.get('sun_pos_vec'), kwargs.get("alpha"))

        self.x = self.x + self.vx * dt + 0.5 * fvec[0] * dt ** 2
        self.y = self.y + self.vy * dt + 0.5 * fvec[1] * dt ** 2
        self.vx = self.vx + fvec[0] * dt
        self.vy = self.vy + fvec[1] * dt
        if 1e4 < abs(self.vx):
            self.vx = 1e4 * self.vx / abs(self.vx)
        if 1e4 < abs(self.vy):
            self.vy = 1e4 * self.vy / abs(self.vy)

        if 1e6 < abs(self.x):
            self.x = 1e6 * self.x / abs(self.x)
        if 1e6 < abs(self.y):
            self.y = 1e6 * self.y / abs(self.y)
        self.line_points.append((self.x + self.xc))
        self.line_points.append((self.y + self.yc))
        if 4000 < len(self.line_points):
            self.line_points = self.line_points[2:]

    def calculate_force(self, sun_pos_vec, alpha):
        """
        Args:
            alpha: the strength of gravitational field scaled to rotate earth every 20 seconds around the screen
            sun_pos_vec: sun position vector as np vector
        Returns:
            the numerical value of force
        """
        self.r = np.linalg.norm(self.pos_vector - sun_pos_vec)
        f = - abs(alpha) / self.r ** 2
        f_vec = (self.pos_vector - sun_pos_vec) * f / self.r
        return f_vec, f
