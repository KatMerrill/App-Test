from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window


class HomePage(Widget):
    pass

class MMApp(App):
    def build(self):
        root_widget = DrawingWidget()
        return root_widget


class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
            Color(0, 0.533, 0.412, 0.8)  # note that we must reset the colour
            Rectangle(size=(Window.width, 100),
                      pos=(0, Window.height - 100))
        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size



if __name__ == '__main__':
    MMApp().run()

