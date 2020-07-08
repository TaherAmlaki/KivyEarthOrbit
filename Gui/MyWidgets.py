from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


class MyLabel(Label):
    def __init__(self, **kwargs):
        self._bg_color = kwargs.get("bg_color", (1, 1, 1, 1))
        kwargs.pop('bg_color', None)
        super().__init__(**kwargs)

    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self._bg_color)
            Rectangle(pos=self.pos, size=(self.size[0] * 0.95, self.size[1]))
