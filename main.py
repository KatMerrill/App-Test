from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

# from kivy.core.video import Video


class MMApp(App):
    def build(self):

        # player = Video(source='sample.mp4')
        # # player.state = 'play'
        # # player.options = {'allow_stretch': True}
        # return(player)

        main_layout = FloatLayout()

        # menu bar contains the website title (button redirecting to main page), search bar, and 3 buttons
        menubar = BoxLayout(
            size_hint = (.5, .25),
            pos_hint = ({'x': .2, 'y': .2}),
            
            
        )

        # page title
        page_title = Label(
            text='Multicast Menu Mobile'
            )
        menubar.add_widget(page_title)

        # search bar
        searchbar = TextInput(
            text = 'Search',
            size_hint = (.6, .25)
            )
        menubar.add_widget(searchbar)

        # View Streams dropdown menu: All Streams, Trending Streams, Editor's Choice Streams
        dropdown = DropDown()
        
        dropdown_choices = [Button(text='Select Stream'), Button(text='All Streams'), Button(text='Trending Streams'), Button(text='Editor\'s Choice Streams')]
        for btn in dropdown_choices[1:]:

            # XXX what does lambda do here
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown_choices[0].bind(on_release=dropdown.open)


        menubar.add_widget(dropdown)

        # Login button
        login_button = Button(
            text = 'Log in'
        )
        menubar.add_widget(login_button)

        # Register button
        register_button = Button(
            text = 'Register'
        )
        menubar.add_widget(register_button)


        main_layout.add_widget(menubar,'top')
        


        
        # layout.add_widget(DrawingWidget())

        # searchbar = TextInput(text = 'Search')
        # layout.add_widget(searchbar)
        return main_layout


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

