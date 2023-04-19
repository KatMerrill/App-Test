from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

 

KV = '''
MDBoxLayout:
    orientation: "vertical"
    ScreenManager:
        id: screen_manager   
        Screen:
            name: "Home"               
              
            MDLabel:
                text: "Screen 1"
                halign: "center"   

        Screen:
            name: "Search"                   
            MDTopAppBar:
                id: toolbar
                pos_hint: {"top": 1}
                elevation: 10
                title: "MDNavigationDrawer"
                left_action_items: [["arrow-left", lambda x: screen_manager.current("scr1")]]                   

            MDLabel:
                text: "Screen 2"
                halign: "center"  

    MDTopAppBar:
        title: "Multicast Mobile"
        screen_manager: screen_manager
        left_action_items:
            [
            ["home", lambda x: app.callback("Home",screen_manager), "Home"]
            ]
        right_action_items:
            [
            ["magnify", lambda x: app.callback("Search",screen_manager), "Search"],
            ["camera", lambda x: app.callback("Record",screen_manager), "Record"],
            ["account", lambda x: app.callback("Account",screen_manager), "Account"]
            ]
'''


class Test(MDApp):
    def callback(self, button_name,screen_manager):
        print(button_name)
        screen_manager.current = button_name
        pass
 
    def build(self):
        return Builder.load_string(KV)

Test().run()