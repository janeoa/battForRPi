import serial

class Battery(object):    
    
    def __init__(self):
        self.serialport = serial.Serial("/dev/serial0", 9600)
        self._vcc = 5.0
        self._low = 3.0
        self._high = 4.2
        self._dV = self._high-self._low

    def getRaw(self):
        raw = self.serialport.readline()
        return int(raw)

    def getVoltage(self):
        raw  = self.serialport.readline()
        voltage = float(float(raw)*self._vcc/1023.0)
        return(voltage)

    def getBattery(self):
        voltage = self.getVoltage()
        percentage = (voltage-self._low)*100.0/self._dV
        return percentage

