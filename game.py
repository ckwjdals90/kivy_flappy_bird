from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.add_widget(Image(source='images/background.png'))
        self.add_widget(Image(source='images/bird.png'))


class GameApp(App):
    def build(self):
        return Game()


if __name__ == "__main__":
    GameApp().run()
