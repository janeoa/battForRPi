# battForRPi

This project uses Attiny85 microcontroller to measure the voltage across 3.7li-ion battery using build-in ADC and sends it via UART to the Raspberry Pi becase RPi does not have an ADC. 
P.S. the idea was bad. Even thought it worked pretty good, the resolution of ADC is pretty small. Reference 5V of raspberry pi could not be trusted.
I would suggest using atmega with internal reference, with some dc offset, however, may be it is better to use dedicated li-ion charging controller with i2c interface like bq25896. It could be powered by 5-15V source, supports fast-charge and even has ADC for both voltage and current. 
