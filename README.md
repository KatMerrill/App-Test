# Multicast Mobile
This app explores non-native multicast streaming for live video content.

Disclaimer: this repository is slightly out of date; currently working to get all changes committed.

### Planned Features + Fixes
- [X] Stream camera to unicast2multicast translator via FFmpeg
- [X] Camera preview
- [X] UI Design
- [X] Add AMT Gateway implementation
- [ ] Integrate AMT Gateway
- [ ] Integrate with Multicast Menu stream scraping
- [ ] Full screen for camera and stream viewing
- [ ] Fix stream encoding
- [ ] Native Multicast?

### Development
For the development environment to work, you will need FFmpeg installed and working on your device. As tested, the development environment works in Linux; the Kivy camera implementation does not work in a Windows development environment.

1. You must download the following libraries (using pip install): kivy, kivymd, pillow, ffpyplayer
2. Run main.py to open the dev environment (demo_main.py is a version of the app that uses dummy thumbnails and videos to mimic viewing a live stream as the AMT gateway has not been integrated yet into the app). 
3. To build for Android or iOS, consult the documentation for Buildozer

### Contribution
Pull requests and feature suggestions welcome!
