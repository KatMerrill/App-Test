from kivy.app import App
from kivy.uix.widget import Widget


class HomePage(Widget):
    pass

class MMApp(App):
    def build(self):
        return HomePage()

if __name__ == '__main__':
    MMApp().run()

