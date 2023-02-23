#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from https://stackoverflow.com/questions/35044166/how-do-i-add-buttons-that-are-dynamically-created-in-pure-python-to-a-kivy-layou

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.clock import mainthread
from kivy.lang import Builder


NUMBER_OF_BUTTONS = 5

# kv = Builder.load_file("test.kv")

class MapScreen(Screen):

    @mainthread
    def on_enter(self):
        for i in range(NUMBER_OF_BUTTONS):
            button = Button(text="B_" + str(i))
            self.ids.grid.add_widget(button)


class Test(App):
    pass


Test().run()