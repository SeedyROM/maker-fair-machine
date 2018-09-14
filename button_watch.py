import wiringpi
import time

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(26, 0)
wiringpi.pullUpDnControl(26, wiringpi.PUD_UP)

try:
    while True:
        if not wiringpi.digitalRead(26):
            print('I am down man!')

        time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    print('Bye bye!')
