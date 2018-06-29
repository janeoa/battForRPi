class Battery:
    import serial
    from gpiozero import LED

    resetPin = LED(18)
    resetPin.off()
    resetPin.on()
    serialport = serial.Serial("/dev/serial0", 9600)

    def getRaw():

    while True:
        command = serialport.readline()
        print str(command)
