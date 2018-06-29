from battery import *

batt = Battery()

while True:
    toOut = "{} {}V {}%".format(batt.getRaw,batt.getVoltage,batt.getBattery)