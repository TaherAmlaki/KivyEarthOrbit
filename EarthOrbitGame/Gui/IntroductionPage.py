from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import CoreMarkupLabel
from Gui.Background import StaticBackground
from Paths import PageNames


class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.force = {}
        self.add_widget(StaticBackground())
        self._description = CoreMarkupLabel(text="[size=50][color=#FFFFFF]Earth Orbit Game[/color][/size]",
                                            markup=True, multiline=False)
        self._description.refresh()
        with self.canvas:
            w, h = self._description.texture.size
            self._text_label = Rectangle(texture=self._description.texture,
                                         pos=(40, Window.height - 2.5 * h),
                                         size=self._description.texture.size)
        self.bind(pos=self._update_rect, size=self._update_rect)

        grid = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.2, 0.2),
                         height=Window.height, pos_hint={'top': 0.35, 'center_x': 0.8})
        grid.bind(height=grid.setter('top'))
        btn = Button(text="Start", background_color=(0, 1, 0, 1), font_size=40)
        btn.bind(on_release=self._on_start_clicked)
        grid.add_widget(btn)
        self.add_widget(grid)

    def _update_rect(self, *args):
        w, h = self._description.texture.size
        self._text_label.pos = (40, Window.height - 2.5 * h)
        self._text_label.size = self._description.texture.size

    def _on_start_clicked(self, instance):
        self.manager.current = PageNames.GAME_PAGE.value
