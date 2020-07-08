from kivy.graphics.vertex_instructions import Ellipse
import numpy as np


class Entity:
    IMAGE = None

    def __init__(self, x=None, y=None, size=None):
        self.x = x
        self.y = y
        self.size = size
        self.vx = 0
        self.vy = 0
        self.force = None
        self.line_points = []

    @property
    def ellipse(self):
        return Ellipse(source=type(self).IMAGE, pos=(self.x, self.y), size=self.size)

    @property
    def pos_vector(self):
        return np.array((self.x, self.y))

    @property
    def pos(self):
        return self.x, self.y

    def move(self, *args, **kwargs):
        pass
