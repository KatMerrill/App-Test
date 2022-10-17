from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
# from kivy.core.video import Video


class MMApp(App):
    def build(self):

        # player = Video(source='sample.mp4')
        # # player.state = 'play'
        # # player.options = {'allow_stretch': True}
        # return(player)

        root_widget = DrawingWidget()

        searchbar = TextInput(text = "Search")
        root_widget.add_widget(searchbar)
        return root_widget


class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size,
                                  pos=self.pos)
            Color(0, 0.533, 0.412, 0.8)
            Rectangle(size=(Window.width, 100),
                      pos=(0, Window.height - 100))
        
        self.bind(pos=self.update_rectangle,
                  size=self.update_rectangle)

        
        

        # player = Video(filename='sample.mp4')
        # player.autoplay = True
        # player.state = 'play'
        # player.options = {'allow_stretch': True}
                
        

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size



if __name__ == '__main__':
    MMApp().run()

