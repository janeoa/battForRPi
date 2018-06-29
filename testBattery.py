from battery import *

batt = Battery()

while True:
    batt.setBattery('3.7','4.2','5.0')
    toOut = '{0:>4}  {1:>2.2}V {2:>3}%'.format(str(batt.getRaw),float(batt.getVoltage),str(batt.getBattery))
    print toOut