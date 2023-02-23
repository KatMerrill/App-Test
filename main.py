from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


# from kivy.core.video import Video

class MMApp(App):
    def build(self):
        Window.maximize()


        main_layout = FloatLayout(
            size_hint = (1, 1),
            pos_hint = {'x' : 0, 'y' : 0}
        )

        # sets background to white
        Window.clearcolor = (1, 1, 1, 1)

        # menu bar contains the website title (button redirecting to main page), search bar, and 3 buttons
        menubar = FloatLayout(
            size_hint = (1, 0.2),
            pos_hint = ({'x': 0, 'y': 0.8}),
        )

        # page title
        # page_title = Label(
        #     text = 'MM',
        #     color = (0, 0, 0, 1),
        #     size_hint = (0.2, 0.2),
        #     pos_hint = {'x' : 0.05, 'y' : 0.4}
        #     )
        # menubar.add_widget(page_title)

        # TODO: search bar should appear when search icon is clicked
        # search bar
        # searchbar = TextInput(
        #     text = 'Search',
        #     size_hint = (0.3, 0.25),
        #     pos_hint = {'x' : 0.3, 'y' : 0.4}
        #     )
        # menubar.add_widget(searchbar)

        # View Streams dropdown menu: All Streams, Trending Streams, Editor's Choice Streams
        dropdown = DropDown(
            size_hint = (0.2, 0.4),
            pos_hint = {'x' : 0.5, 'y' : 0.1}
        )
        
        # TODO: dropdown currently doesn't work :)
        # dropdown_choices = [
        #     Button(text='Select Stream', size_hint = (None, None)), 
        #     Button(text='All Streams', size_hint_y=None, height=44), 
        #     Button(text='Trending Streams', size_hint_y=None, height=44), 
        #     Button(text='Editor\'s Choice Streams', size_hint_y=None, height=44)]
        # for btn in dropdown_choices[1:]:
        #     btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        #     dropdown.add_widget(btn)
        # dropdown_choices[0].bind(on_release=dropdown.open)
        # dropdown.bind(on_select=lambda instance, x: setattr(dropdown_choices[0], 'text', x))
        # menubar.add_widget(dropdown)

        # Search button
        search_button = Button(
            background_normal = 'images/search.PNG',
            size_hint = (0.2,0.5),
            pos_hint = {'x' : 0.1, 'y' : 0.2}
        )
        menubar.add_widget(search_button)

        # Record button
        record_button = Button(
            background_normal = 'images/record.PNG',
            size_hint = (0.2,0.5),
            pos_hint = {'x' : 0.4, 'y' : 0.2}
        )
        menubar.add_widget(record_button)

        # Account button
        account_button = Button(
            background_normal = 'images/account.PNG',
            size_hint = (0.2,0.5),
            pos_hint = {'x' : 0.7, 'y' : 0.2}
        )
        menubar.add_widget(account_button)
        
        
        main_layout.add_widget(menubar)

        scrollview = ScrollView(
            size_hint = (1, 0.8),
            pos_hint = {'x' : 0, 'y' : 0}
        )
        scrolling_layout = FloatLayout(
            size_hint = (1, 1.5)
        )

        # XXX what are we doing :)
        # video = Video(
        #     source='sample.mp4',
        #     size_hint = (0.5, 0.5),
        #     pos = (0, 0)
        # )
        # scrolling_layout.add_widget(video)

        placeholder_streams = []
        for num in range((count_streams := 3)):
            placeholder_streams.append(
                Button(
                    size_hint = (0.75, 0.2),
                    pos_hint = {'x' : 0.05, 'y' : 0.1 + ((3 * num) // count_streams)/10 * 2.5},
                    background_normal = '',
                    background_color = (0, 0.533, 0.412, 1)
                ))
            scrolling_layout.add_widget(placeholder_streams[num])

        instructions = Label(
            text = 'Available streams are listed below:',
            size_hint = (0.6, 0.2),
            pos_hint = {'x' : 0.2, 'y' : 0.85},
            color = (0, 0, 0, 1)
        )
        scrolling_layout.add_widget(instructions)

        scrollview.add_widget(scrolling_layout)
        main_layout.add_widget(scrollview)

        return main_layout


if __name__ == '__main__':
    MMApp().run()
