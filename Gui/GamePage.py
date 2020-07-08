from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.screenmanager import Screen
from random import uniform
from math import pi, cos, sin
from Gui.Background import StaticBackground
from Gui.SpeedGrid import SpeedGrid
from Entities import EarthEntity, SunEntity


class GameScreen(Screen):
    OMEGA = 0.1 * pi

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(StaticBackground())
        self._force = None
        self._keyboard = None
        self._keys_pressed = set()
        self._request_keyboard()

        with self.canvas:
            self.radius = min(Window.width, Window.height) * 0.5 - 50
            self._theta = uniform(0, 2 * pi)
            self.xo = Window.width * 0.5 - 50
            self.yo = Window.height * 0.5 - 50
            self.alpha = self.OMEGA ** 2 * self.radius ** 3
            self._earth = EarthEntity.Earth(x=self.xo + self.radius * cos(self._theta),
                                            y=self.yo + self.radius * sin(self._theta), size=(50, 50))
            self._sun = SunEntity.Sun(x=self.xo, y=self.yo, size=(50, 50))
            self._earth_ellipse = self._earth.ellipse
            self._sun_ellipse = self._sun.ellipse
            Color(0, 0, 1, 1)
            self._earth_line = Line(points=[self._earth.x, self._earth.y], width=2.0)
            Color(1, 1, 0, 1)
            self._sun_line = Line(points=[self._sun.x, self._sun.y], width=1.0, dash_length=1)

        self._speed_grid = SpeedGrid(pause_callback=self._on_pause_clicked, speed_updated=self._update_speed,
                                     reset_callback=self._reset_callback)
        self.add_widget(self._speed_grid.grid)

        self.bind(size=self._update_ellipses)
        self._clock = None

    def _move(self, dt):
        self._sun.move(self._keys_pressed, dt)
        self._sun_ellipse.pos = self._sun.pos
        self._sun_line.points = self._sun.line_points
        self._earth.move(dt=dt, sun_pos_vec=self._sun.pos_vector, alpha=self.alpha)
        self._earth_ellipse.pos = self._earth.pos
        self._earth_line.points = self._earth.line_points

    def _update_ellipses(self, *args):
        self.radius = min(Window.width, Window.height) * 0.5 - 50
        self.alpha = self.OMEGA ** 2 * self.radius ** 3
        self.xo = Window.width * 0.5 - 50
        self.yo = Window.height * 0.5 - 50
        self._sun.x = self.xo
        self._sun.y = self.yo
        self._sun_ellipse.pos = self._sun.pos
        self._earth.x = self.xo + self.radius * cos(self._theta)
        self._earth.y = self.yo + self.radius * sin(self._theta)
        self._earth_ellipse.pos = self._earth.pos

    def _request_keyboard(self):
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self._keys_pressed = set()

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None
        self._keys_pressed = set()

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        text = keycode[1]
        self._keys_pressed.add(text)

    def _on_key_up(self, keyboard, keycode):
        if keycode[1] in self._keys_pressed:
            self._keys_pressed.remove(keycode[1])

    def _on_pause_clicked(self, instance):
        if instance.text == "Start":
            speed = {}
            for name in ['vx', 'vy']:
                speed[name] = round(getattr(self._speed_grid, name).value, 1)
            self._earth.vx = speed['vx']
            self._earth.vy = speed['vy']
        if instance.text == "Pause":
            self._clock.cancel()
            self._clock = None
            self._speed_grid.pause_btn.text = "Continue"
        elif instance.text in ["Continue", 'Start']:
            self._clock = Clock.schedule_interval(self._move, 0)
            self._speed_grid.pause_btn.text = "Pause"

    def _update_speed(self):
        speed = {}
        for name in ['vx', 'vy']:
            speed[name] = round(getattr(self._speed_grid, name).value, 1)
        self._earth.vx = speed['vx']
        self._earth.vy = speed['vy']

    def _reset_callback(self, instance):
        try:
            self._clock.cancel()
        except AttributeError:
            pass
        self._clock = None
        self._speed_grid.pause_btn.text = "Start"
        self.radius = min(Window.width, Window.height) * 0.5 - 50
        self.alpha = self.OMEGA ** 2 * self.radius ** 3
        self.xo = Window.width * 0.5 - 50
        self.yo = Window.height * 0.5 - 50

        self._sun.x = self.xo
        self._sun.y = self.yo
        self._sun_ellipse.pos = self._sun.pos
        self._sun.line_points = [self._sun.x + self._sun.xc, self._sun.y + self._sun.yc]
        self._sun_line.points = self._sun.line_points

        self._earth.x = self.xo + self.radius * cos(self._theta)
        self._earth.y = self.yo + self.radius * sin(self._theta)
        self._earth_ellipse.pos = self._earth.pos
        self._earth.line_points = [self._earth.x + self._earth.xc, self._earth.y + self._earth.yc]
        self._earth_line.points = self._earth.line_points

