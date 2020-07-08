from enum import Enum


class ForceAppPath(Enum):
    BACKGROUND = "./assets/milky-way.jpg"
    FORCE_ICON = "./assets/force_icon.png"
    EARTH_IMAGE = "./assets/earth.jpg"
    SUN_IMAGE = "./assets/sun.jpg"

    @property
    def path(self):
        return self.value


class PageNames(Enum):
    INTRO = "introPage"
    GAME_PAGE = "gamePage"
