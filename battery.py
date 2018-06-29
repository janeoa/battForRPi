import serial

class Battery:    
    serialport = serial.Serial("/dev/serial0", 9600)

    _vcc = 5.0
    _low = 3.0
    _high = 4.2
    _dV = _high-_low

    def getRaw():
        raw = serialport.readline()
        return str(raw)

    def getVoltage():
        raw  = serialport.readline()
        voltage = float(float(raw)*_vcc/1023.0)
        return(voltage)

    def getBattery():
        voltage = getVoltage()
        percentage = (voltage-_low)*100.0/_dV
        return percentage

