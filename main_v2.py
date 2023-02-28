from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import mainthread

Window.clearcolor = (255, 255, 255, 255)
Window.maximize()
# used to load a file other than the default, which is my.kv
kv = Builder.load_file("myApp.kv")

# defines a custom button class used for the buttons that link to streams
class StreamButton(Button):
    pass

stream_urls = ['temp1', 'temp2', 'temp3']
stream_buttons = []

# all classes referred to in the .kv files don't need any code here. Note that this inherits from Screen
class HomeScreen(Screen):
    @mainthread
    def on_enter(self):
        for num in range(stream_count:=len(stream_urls)):
            # note that these are placeholders, but real streams will be stored in some sort of list similar to this
            stream_buttons.append(
                StreamButton(
                    # all other aspects of the button are defined 
                    pos_hint = {'x' : 0.05, 'y' : 0.1 + ((3 * num) // stream_count)/10 * 2.5}
                )
            )
            self.ids.scrolling_layout.add_widget(stream_buttons[num])

class WatchScreen(Screen):
    pass

# the app only has to build itself, since everything else is contained in the .kv files
class MyMainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(WatchScreen())  
        sm.current = 'main_screen'
        return sm

if __name__ == "__main__":
    MyMainApp().run()
