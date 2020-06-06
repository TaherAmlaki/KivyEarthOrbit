from Entities.BaseEntity import Entity
from Paths import ForceAppPath


class Sun(Entity):
    IMAGE = ForceAppPath.SUN_IMAGE.path

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line_points = []
        self.xc = self.size[0] * 0.5
        self.yc = self.size[1] * 0.5

    def move(self, keys_pressed, dt):
        step = 100 * dt
        is_moving = False
        if 'right' in keys_pressed:
            self.x += step
            is_moving = True
        if 'left' in keys_pressed:
            self.x -= step
            is_moving = True
        if 'up' in keys_pressed:
            self.y += step
            is_moving = True
        if 'down' in keys_pressed:
            self.y -= step
            is_moving = True
        if is_moving:
            self.line_points.append(self.x + self.xc)
            self.line_points.append(self.y + self.yc)
            if 4000 < len(self.line_points):
                self.line_points = self.line_points[2:]
