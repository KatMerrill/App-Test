from kivy.app import App
from kivy.uix.video import Video

class VideoWindow(App):
    def build(self):
        video = Video(source = 'sample.mp4')
        video.state = "play"
        video.options = {'eos': 'loop'}

        video.allow_stretch = True

        return video


def main():
    window = VideoWindow()
    window.run()

if __name__ == '__main__':
    main()