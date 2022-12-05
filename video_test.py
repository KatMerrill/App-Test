from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

class VideoWindow(App):
    def build(self):
        video = VideoPlayer(source = 'sample.mp4')
        video.state = "play"
        video.options = {'eos': 'loop'}
        video.options = {'allow_stretch' : 'True'}

        return video


def main():
    window = VideoWindow()
    window.run()

if __name__ == '__main__':
    main()