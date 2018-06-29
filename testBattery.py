from battery import *

batt = Battery()

while True:
    print(str(batt.getRaw())+'    '+str(batt.getVoltage())+'V '+str(batt.getVoltage())+'%')