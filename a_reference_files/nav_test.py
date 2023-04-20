from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Multicast Mobile"
        left_action_items:
            [
            ["home", lambda x: app.callback("Home"), "Home"]
            ]
        right_action_items:
            [
            ["magnify", lambda x: app.callback("Search"), "Search"],
            ["camera", lambda x: app.callback("Record"), "Record"],
            ["account", lambda x: app.callback("Account"), "Account"]
            ]

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Test(MDApp):
    def callback(x, button_name):
        print(button_name)
        # root.manager.current = button_name
        pass

    def build(self):
        return Builder.load_string(KV)


Test().run()