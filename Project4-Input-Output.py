import explorerhat as eh
from time import sleep

while True:
    if eh.input.one.read() == 1:
        eh.output.one.toggle()
        eh.light.toggle()
        sleep(0.5)
