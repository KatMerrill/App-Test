from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Test(MDApp):
    def callback(self, button_name, screen_manager, optional_url = ""):
        print(button_name)
        # screen_manager.transition.direction = 'right'
        screen_manager.current = button_name
        if(button_name == "Record"):
            record_video()
        if(button_name == "Watch"):
             watch_video(optional_url)
        

    def build(self):
        my_app = Builder.load_file("myApp.kv")

        scrollview = ScrollView(
            size_hint = (1, 0.8),
            pos_hint = {'x' : 0, 'y' : 0}
        )
        scrolling_layout = FloatLayout(
            size_hint = (1, 1.5)
        )

        stream_urls = ["a", "b", "c"]
        stream_buttons = []
        for num in range((stream_count := len(stream_urls))):
            stream_buttons.append(
                Button(
                    size_hint = (0.75, 0.2),
                    pos_hint = {'x' : 0.05, 'y' : 0.1 + ((3 * num) // stream_count)/10 * 2.5},
                    background_normal = '',
                    background_color = (0, 0.533, 0.412, 1),
                    # on_release = {
                    #     self.callback("Videoplayer", my_app.ids.screen_manager, stream_buttons[num])
                    # }
                ))
            scrolling_layout.add_widget(stream_buttons[num])
        scrollview.add_widget(scrolling_layout)
        my_app.ids.home.add_widget(scrollview)

        return my_app


def watch_video():
        pass

def record_video():
    pass

Test().run()