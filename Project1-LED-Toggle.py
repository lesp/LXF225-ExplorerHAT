import explorerhat as eh
from time import sleep

while True:
    if eh.touch.one.is_pressed():
        eh.light.blue.toggle()
        sleep(0.1)
    elif eh.touch.two.is_pressed():
        eh.light.yellow.toggle()
        sleep(0.1)
    elif eh.touch.three.is_pressed():
        eh.light.red.toggle()
        sleep(0.1)
    elif eh.touch.four.is_pressed():
        eh.light.green.toggle()
        sleep(0.1)
