import webbrowser as web
import keyboard as kb
import time

web.open(r'www.google.com')
time.sleep(1)
kb.press_and_release('ctrl+N')
web.open(r'https://scratch.mit.edu/')
time.sleep(2)
kb.press_and_release('f11')
time.sleep(1)
kb.press_and_release('ctrl+0')
