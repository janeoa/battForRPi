from battery import *

batt = Battery()

while True:
    batt.setBattery('3.7','4.2','5.0')
    toOut = '{0:>4}  {1:>2.2}V {2:>3}%'.format(batt.getRaw,batt.getVoltage,batt.getBattery)
    print toOut