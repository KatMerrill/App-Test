from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp

Window.clearcolor = (255, 255, 255, 255)


Window.maximize()
Window.size = (300, 500) # FOR TESTING, remove before compiling


# used to load a file other than the default (default is my.kv)


# defines a custom button class used for the buttons that link to streams
class StreamButton(Button):
    pass

class MenuBar(FloatLayout):
    pass

stream_urls = ['temp1', 'temp2', 'temp3']
stream_buttons = []

# all classes referred to in the .kv files don't need any code here. Note that this inherits from Screen
class HomeScreen(Screen):
# self.theme_cls.primary_palette = ...
    pass

class WatchScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class MyManager(ScreenManager):
    def switch_page(x, page):
        print(page)
        current = 'screen2'
    pass

class ScreenNav(ScreenManager):
    pass

class MyMainApp(MDApp):
    def build(self):
        self.root = Builder.load_file("test_combine.kv")
        # sm = MyManager()
        # sm.add_widget(HomeScreen())
        # sm.add_widget(WatchScreen())
        # sm.add_widget(AccountScreen())  
        # sm.current = 'main_screen'
        # return sm
        
    

    # def switch_page(x, button_name): 
    #     sm.current = button_name
        # pass
    
    

if __name__ == "__main__":
    MyMainApp().run()
