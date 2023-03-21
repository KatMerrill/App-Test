from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Multicast Mobile"
        left_action_items:
            [
            ["home", lambda x: app.callback(x), "Home"]
            ]
        right_action_items:
            [
            ["magnify", lambda x: app.callback(x), "Search"],
            ["camera", lambda x: app.callback(x), "Record"],
            ["account", lambda x: app.callback(x), "Account"],
            ]

    MDLabel:
        text: "Content"
        halign: "center"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()