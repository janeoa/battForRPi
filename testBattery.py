from battery import *

batt = Battery()

while True:
    toOut = "{0} {1:.2}V {2}%".format(batt.getRaw,batt.getVoltage,batt.getBattery)