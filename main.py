from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import mainthread
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp


Window.clearcolor = (255, 255, 255, 255)
Window.maximize()
# used to load a file other than the default (default is my.kv)
kv = Builder.load_file("myApp.kv")

# defines a custom button class used for the buttons that link to streams
class StreamButton(Button):
    pass

class MenuBar(FloatLayout):
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

class AccountScreen(Screen):
    pass

class MyManager(ScreenManager):
    pass

class MyMainApp(App):
    # def callback(x, button_name):
        # manager.current = button_name
        # pass
    
    def build(self):
        sm = MyManager()
        # sm.add_widget(HomeScreen())
        # sm.add_widget(WatchScreen())
        # sm.add_widget(AccountScreen())  
        sm.current = 'main_screen'
        return sm

if __name__ == "__main__":
    MyMainApp().run()
