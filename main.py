# general app imports
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from functools import partial

# for video streaming
import subprocess
from kivy.clock import Clock
from PIL import Image as PILImage


class Test(MDApp):
    # callback function is called when any button is pressed (both static and dynamic). redirects to correct page
    def callback(self, instance, my_manager, button_name = "Watch", vid_url = ""):
        my_manager.current = button_name

        # for temporary video only
        stream_player = self.root.ids.stream_player
        stream_player.state = 'stop'

        if(button_name == "Record"):
            record_video()
        if(button_name == "Watch"):
            self.watch_video(my_manager, vid_url)
        
    # loads the kivy file
    def build(self):
        my_app = Builder.load_file("myApp.kv")

        # before compiling into an apk, switch to this!!
        # Window.maximize()
        Window.size = (450, 800)
        Window.size = (400, 710)

        scrollview = ScrollView(
            size_hint = (1, 0.9),
            pos_hint = {'x' : 0, 'y' : 0},
        )
        scrolling_layout = FloatLayout(
            size_hint = (1, 1.5)
        )

        stream_urls = ["a", "b", "c", "d"]
        stream_buttons = []
        for num in range((stream_count := len(stream_urls))):
            stream_buttons.append(
                Button(
                    size_hint = (0.8, 0.2),
                    pos_hint = {'x' : 0.1, 'y' : 0.1 + ((3 * num) // stream_count)/10 * 2.5},
                    background_normal = '',
                    background_color = (0, 0.533, 0.412, 1),
                ))
            
            # when a dynamic (stream) button is pressed, it calls the callback function
            stream_buttons[num].bind(on_press=partial(self.callback, my_manager=my_app.ids.screen_manager, vid_url=stream_urls[num]))

            scrolling_layout.add_widget(stream_buttons[num])
        scrollview.add_widget(scrolling_layout)
        my_app.ids.home.add_widget(scrollview)

        # for video stream
        self.send_frame = False
        self.current_frame = None
        self.prev_frame = None
        self.streamEvent = None

        return my_app
    
    def startstop(self): # run on main thread
        print(self.root.ids.button.text)
        self.send_frame = not self.send_frame
        if self.send_frame:
            self.root.ids.button.text = "Stop Video"
            streamProcess = open_ffmpeg_stream_process()
            self.streamPipe = streamProcess
            self.streamEvent = Clock.schedule_interval(self.updateCurrFrame, 1/30)
        else:
            self.root.ids.button.text = "Start Video" 
            self.streamEvent.cancel()
    
    def updateCurrFrame(self, dt):
        self.prev_frame = self.current_frame
        self.current_frame = PILImage.frombytes('RGBA', self.root.ids.camera.texture.size, self.root.ids.camera.texture.pixels)
        self.streamPipe.stdin.write(self.current_frame.tobytes())


    def watch_video(self, instance, vid_url):
        stream_player = self.root.ids.stream_player
        stream_player.source = 'a_video_test/sample.mp4'
        stream_player.state = 'play'
        stream_player.options = {'eos': 'loop', 'allow_stretch' : 'True'}


def record_video():
    pass

# srt://3.89.162.77:9997
def open_ffmpeg_stream_process(): # paramertize this to allow for different urls
    args = (
        "ffmpeg -re -f rawvideo -pix_fmt rgba -s:v 1280x720 -framerate 30 -i pipe:0 -c:v libx264 -preset ultrafast -pix_fmt yuv420p -f mpegts udp://127.0.0.1:1234?pkt_size=1316"
    ).split()
    return subprocess.Popen(args, stdin=subprocess.PIPE)


Test().run()