from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# used to load a file other than the default, which is my.kv
kv = Builder.load_file("myApp.kv")

# the app only has to build itself, since everything else is contained in the .kv files
class MyMainApp(App):
    def build(self):
        return kv

# all classes referred to in the .kv files don't need any code here. Note that this inherits from Screen
class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

# ScreenManager keeps track of all Screens
class WindowManager(ScreenManager):
    pass

if __name__ == "__main__":
    MyMainApp().run()
