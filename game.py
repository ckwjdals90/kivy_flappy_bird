from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class Game(Widget):
    pass


class GameApp(App):
    def build(self):
        return Game(size=Window.size)


if __name__ == "__main__":
    GameApp().run()
