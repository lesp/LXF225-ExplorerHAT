import explorerhat as eh

while True:
        speed = (round(eh.analog.one.read()) * 20)
        eh.motor.one.forward(speed)

