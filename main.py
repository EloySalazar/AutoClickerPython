import threading
import time
import pynput
from pynput.mouse import Controller,Button
from pynput.keyboard import Listener,KeyCode

delay = 0.001
buton = Button.left

start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self,delay,button):
        super().__init__()

        self.delay = delay
        self.button = button

        self.running = False

        self.program_running = True

    def start_click(self):
        self.running =  True

    def stop_click(self):
        self.running = False

    
    def exit(self):
        self.stop_click()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(delay)


print("Press ",start_stop_key.char,"start")
print("Press ",exit_key,"exit")
mouse = Controller()
click_t = ClickMouse(delay,buton)
click_t.start()

def on_press(key):
    if key == start_stop_key:
        if click_t.running:
            click_t.stop_click()

        else:
            click_t.start_click()

    elif key == exit_key:
        click_t.exit()
        listener.stop()
        

with Listener(on_press=on_press) as listener:
    listener.join()

