#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time


def my_callback(channel):
    global lasttime
    global times
    nowtime = time.perf_counter()
    delta = (nowtime - lasttime) * 1000
    lasttime = nowtime
    if GPIO.input(port):
        times.append((delta, 1))
    else:
        times.append((delta, 0))


if __name__ == '__main__':
    bytelen = 4
    port = 27
    lasttime = time.perf_counter()
    data = ''
    pardata, times = [], []
    word = ''

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(port, GPIO.IN)
    if False:
        GPIO.add_event_detect(port, GPIO.BOTH, callback=my_callback)
        try:
            while True:
                time.sleep(5)
                printvalues = times
                times = []
                with open('data.csv', 'a') as outfile:
                    for value in printvalues:
                        outfile.write(str(value[0]) + ',' + str(value[1]) + '\n')
        except KeyboardInterrupt:

            print('\nShutdown')
        finally:
            GPIO.cleanup()
    else:
        try:
            f = open('data2.csv', 'a')
            while True:
                time.sleep(0.00001)     # ~44,1kHz
                if GPIO.input(port):
                    f.write('1')
                else:
                    f.write('0')
        except KeyboardInterrupt:
            pass
        finally:
            f.close()
            GPIO.cleanup()

