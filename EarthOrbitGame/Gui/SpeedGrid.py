from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from Gui.MyWidgets import MyLabel


class SpeedGrid:

    def __init__(self, pause_callback: callable, speed_updated: callable, reset_callback: callable):
        self.force = {}
        self.speed_updated = speed_updated
        self.grid = BoxLayout(orientation='vertical', spacing=5, size_hint=(0.35, 0.15),
                              height=Window.height * 0.5, pos_hint={'top': 0.97, 'center_x': 0.8})
        self.grid.bind(height=self.grid.setter('top'))
        self.grid.add_widget(self._add_speed_label_and_input("vx"))
        self.grid.add_widget(self._add_speed_label_and_input("vy"))
        g = GridLayout(cols=2)
        self.pause_btn = Button(text="Start", background_color=(0, 1, 0, 1), pos=(Window.width-150, 20))
        self.pause_btn.bind(on_release=pause_callback)
        self.reset_btn = Button(text="Reset", background_color=(0, 1, 0, 1), pos=(Window.width - 150, 20))
        self.reset_btn.bind(on_release=reset_callback)
        g.add_widget(self.pause_btn)
        g.add_widget(self.reset_btn)
        self.grid.add_widget(g)

    def _add_speed_label_and_input(self, name: str):
        g = GridLayout(cols=3, padding=[2]*4)
        label = MyLabel(text=name, bg_color=(1, 0, 0, 1), size_hint_x=0.15)
        g.add_widget(label)
        slider = Slider(orientation='horizontal', value_track=True, value_track_color=[0, 0, 1, 1],
                        min=-100, max=100, step=1, value=0.0, size_hint_x=0.7)
        slider.bind(value=self._on_slider_value_updated)
        setattr(self, name, slider)
        g.add_widget(slider)

        label = MyLabel(text="0.0", bg_color=(1, 0, 0, 1), size_hint_x=0.15)
        setattr(self, f"{name}_value", label)
        g.add_widget(label)
        return g

    def _on_slider_value_updated(self, *args):
        for name in ['vx', 'vy']:
            val = round(getattr(self, name).value, 1)
            print(name, val)
            label = MyLabel(text=str(val), bg_color=(1, 0, 0, 1), size_hint_x=0.15)
            setattr(self, f"{name}_value", label)
        self.speed_updated()
