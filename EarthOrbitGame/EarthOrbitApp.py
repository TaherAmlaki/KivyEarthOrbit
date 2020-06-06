from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from Gui.IntroductionPage import IntroductionScreen
from Gui.GamePage import GameScreen
from Paths import PageNames, ForceAppPath


class EarthOrbitApp(App):
    title = "Earth Orbit Game"

    def __init__(self, **kwargs):
        self.icon = ForceAppPath.FORCE_ICON.value
        super().__init__(**kwargs)
        self.sm = ScreenManager(transition=SlideTransition(duration=1))
        self._intro_page = IntroductionScreen(name=PageNames.INTRO.value)
        self._game_page = GameScreen(name=PageNames.GAME_PAGE.value)
        self.sm.add_widget(self._intro_page)
        self.sm.add_widget(self._game_page)
        self._popup_exit = None

    def build(self):
        self.icon = ForceAppPath.FORCE_ICON.value
        Window.clearcolor = (0.25, 0.25, 0.25, 1)
        Window.bind(on_request_close=self.on_request_close)
        return self.sm

    def on_request_close(self, *args, **kwargs):
        if kwargs.get("source") != 'keyboard':
            self.textpopup(title='Exit', text='Do you want to close the app?')
        return True

    def textpopup(self, title='', text=''):
        box = GridLayout(cols=1, size_hint_x=0.25)
        box.add_widget(Label(text=text))

        button_grid = GridLayout(cols=2, size_hint_x=0.5, size_hint_y=0.35)
        ok_button = Button(text='YES', size_hint=(0.25, 0.3))
        ok_button.bind(on_release=self.stop)
        button_grid.add_widget(ok_button)
        cancel_button = Button(text="NO", size_hint=(0.25, 0.3))
        cancel_button.bind(on_release=lambda *args: self._popup_exit.dismiss())
        button_grid.add_widget(cancel_button)

        box.add_widget(button_grid)
        self._popup_exit = Popup(title=title, content=box, size_hint=(0.3, 0.4))
        self._popup_exit.open()


if __name__ == "__main__":
    app = EarthOrbitApp()
    try:
        app.run()
    except Exception as ex:
        raise ex
