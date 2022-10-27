from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

# from kivy.core.video import Video


class MMApp(App):
    def build(self):
        main_layout = FloatLayout(
            size_hint = (1, 1),
            pos_hint = {'x' : 0, 'y' : 0}
        )

        # menu bar contains the website title (button redirecting to main page), search bar, and 3 buttons
        menubar = FloatLayout(
            size_hint = (1, 0.2),
            pos_hint = ({'x': 0, 'y': 0.8}),
        )

        # there are currently errors with this background -- it's showing at the bottom of the screen instead of the top
        # background = DrawingWidget()
        # menubar.add_widget(background)

        # page title
        page_title = Label(
            text='Multicast Menu Mobile',
            size_hint = (0.2, 0.2),
            pos_hint = {'x' : 0.05, 'y' : 0.4}
            )
        menubar.add_widget(page_title)

        # search bar
        searchbar = TextInput(
            text = 'Search',
            size_hint = (0.3, 0.25),
            pos_hint = {'x' : 0.3, 'y' : 0.4}
            )
        menubar.add_widget(searchbar)

        # View Streams dropdown menu: All Streams, Trending Streams, Editor's Choice Streams
        dropdown = DropDown()
        
        # XXX TODO: dropdown currently doesn't work :)

        dropdown_choices = [Button(text='Select Stream'), Button(text='All Streams'), Button(text='Trending Streams'), Button(text='Editor\'s Choice Streams')]
        for btn in dropdown_choices[1:]:

            # XXX what does lambda do here
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown_choices[0].bind(on_release=dropdown.open)


        menubar.add_widget(dropdown)

        # Login button
        login_button = Button(
            text = 'Log in',
            size_hint = (0.1, 0.2),
            pos_hint = {'x' : 0.7, 'y' : 0.4}
        )
        menubar.add_widget(login_button)

        # Register button
        register_button = Button(
            text = 'Register',
            size_hint = (0.1, 0.2),
            pos_hint = {'x' : 0.8, 'y' : 0.4}
        )
        menubar.add_widget(register_button)
        main_layout.add_widget(menubar)


        scrollview = ScrollView(
            size_hint = (1, 0.8),
            pos_hint = {'x' : 0, 'y' : 0}
        )
        scrolling_layout = FloatLayout(
            size_hint = (1, 1.5)
        )
        scrollview.add_widget(scrolling_layout)


        placeholder_streams = []
        for x in range(9):
            placeholder_streams.append(
                Button(
                    size_hint = (0.25, 0.2),
                    pos_hint = {'x' : 0.05 + ((3 * x) % 9)/10, 'y' : 0.1 + ((3 * x) // 9)/10 * 2.5}
                ))
            scrolling_layout.add_widget(placeholder_streams[x])

        main_layout.add_widget(scrollview)

        return main_layout


# extends the Widget class to have a custom canvas
class DrawingWidget(Widget):
    def __init__(self):
        super(DrawingWidget, self).__init__()

        self.size_hint = (1, 1)

        # for whatever reason, this is allowing me to put the rectangle outside of where the drawing class actually is.
        with self.canvas:

            # Color(1, 1, 1, 1)
            # self.rect = Rectangle(
            # )
            Color(0, 0.533, 0.412, 1)
            self.rect = Rectangle(pos = (self.width / 2., self.height / 2.),
                                  size =(self.width / 2.,
                                        self.height / 2.))
        
        self.bind(pos = self.update_rect,
                  size = self.update_rect)

    # update function which makes the canvas adjustable. FROM GEEKS FOR GEEKS - rework this and the self.rect part above
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

        # player = Video(filename='sample.mp4')
        # player.autoplay = True
        # player.state = 'play'
        # player.options = {'allow_stretch': True}
                


if __name__ == '__main__':
    MMApp().run()

