import explorerhat as eh

while True:
    on = eh.analog.one.read()
    off = eh.analog.one.read()
    if on == 0 and off == 0:
        on = 0.01
        off = 0.01
    eh.light.blink(on,off)
        
