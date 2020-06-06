from kivy.graphics.context_instructions import Color
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from Paths import ForceAppPath


class StaticBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1.0, 0.5, 1.0, 0.3)
            self.bg = Rectangle(source=ForceAppPath.BACKGROUND.value, pos=self.pos, size=self.size)
        with self.canvas.after:
            Color(1, 1, 1, 1)
        self.bind(pos=self.update_bg)
        self.bind(size=self.update_bg)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
