import subprocess
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from PIL import Image as PILImage

# from jnius import autoclass
# from android.permissions import request_permissions, Permission
# request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE])

class MainScreen(Screen):
    pass
    
class Manager(ScreenManager):
    pass

# srt://3.89.162.77:9997
def open_ffmpeg_stream_process(): # paramertize this to allow for different urls
    args = (
        "ffmpeg -re -f rawvideo -pix_fmt rgba -s:v 1280x720 -framerate 30 -i pipe:0 -c:v libx264 -preset ultrafast -pix_fmt yuv420p -f mpegts udp://127.0.0.1:1234?pkt_size=1316"
    ).split()
    return subprocess.Popen(args, stdin=subprocess.PIPE)

Builder.load_string('''
<MainScreen>:
    name: "Test"

    FloatLayout:
        Label:
            text: "Webcam from OpenCV?"
            pos_hint: {"x":0.0, "y":0.8}
            size_hint: 1.0, 0.2

        # Camera:
        #     id: camera
        #     resolution: (1920, 1080)
        #     play: True

        Button:
            id: button
            text: 'Start Video'
            pos_hint: {"x":0.0, "y":0.0}
            size_hint: 1.0, 0.2
            font_size: 50
            on_release: app.startstop()
''')


class Main(App):
    def build(self):
        sm = ScreenManager()
        self.main_screen = MainScreen()
        sm.add_widget(self.main_screen)
        # self.main_screen.ids.button.on_release = self.startstop
        self.send_frame = False
        self.current_frame = None
        self.prev_frame = None
        self.streamEvent = None
        return sm

    def startstop(self): # run on main thread
        self.send_frame = not self.send_frame
        
        if self.send_frame:
            self.main_screen.ids.button.text = "Stop Video"
            streamProcess = open_ffmpeg_stream_process()
            self.streamPipe = streamProcess
            self.streamEvent = Clock.schedule_interval(self.updateCurrFrame, 1/30)
        else:
            self.main_screen.ids.button.text = "Start Video" 
            self.streamEvent.cancel()
    
    def updateCurrFrame(self, dt):
        self.prev_frame = self.current_frame
        self.current_frame = PILImage.frombytes('RGBA', self.main_screen.ids.camera.texture.size, self.main_screen.ids.camera.texture.pixels)
        self.streamPipe.stdin.write(self.current_frame.tobytes())
                    
if __name__ == '__main__':
    Main().run()

# vlc -vvv --amt-relay 162.250.137.254 --amt-native-timeout 1 amt://162.250.138.11@232.47.93.134