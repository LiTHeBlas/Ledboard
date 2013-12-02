#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import sys
import time

class monitor:
    def __init__(self):
        self.port = serial.Serial('/dev/tty.usbmodem411')

    def output(self,msg):
        words = msg.split()
        acc = ""
        for w in words:
            if len(acc) + len(acc) + 1 < 16:
                acc = acc + " " + w
            else:
                self.port.write(acc)
                acc = ""
                time.sleep(500)
        
        if len(acc) != 0:
            self.port.write(acc)

        self.port.write(msg)

    def write(self,msg):
        msg = msg.replace("å",chr(140))
        msg = msg.replace("ä",chr(138))
        msg = msg.replace("ö",chr(154))
        msg = msg.replace("Å",chr(129))
        msg = msg.replace("Ä",chr(128))
        msg = msg.replace("Ö",chr(133))
        self.port.write(msg)

    def readAll(self):
        time.sleep(1)
        while True:
            if self.port.inWaiting() != 0 :
                print(self.port.read())
            else:
                break;


if __name__ == "__main__":
    args = sys.argv[1:]
    m = monitor()
    m.write(args[0])
    m.readAll()