import subprocess
from pynput.keyboard import Key, Controller
keyboard = Controller()

subprocess.call(['python', '-m', 'pylivestream.camera', 'localhost', './pylivestream.json', '-y'])
