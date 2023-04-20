from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp


class Test(MDApp):
    def callback(self, button_name, screen_manager):
        print(button_name)
        # screen_manager.transition.direction = 'right'
        screen_manager.current = button_name
        pass
 
    def build(self):
        return Builder.load_file("myApp.kv")

Test().run()