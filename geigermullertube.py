#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 17:13:43 2022

@author: school
"""

import io
import time
import serial


# create filename
FILENAME = 'GMt%s.txt' % (time.strftime('%Y%m%d-%H%M%S', time.localtime()))
SERIALPORT = '/dev/ttyUSB0'
BAUDRATE = 9600


if __name__ == '__main__':
    # open de file in 'append' mode.
    with open(FILENAME, 'a') as stream:
        # print filename:
        print(FILENAME)
        
        # open serial port
        with serial.Serial(SERIALPORT, BAUDRATE, timeout=10) as ser:
            # create readline buffer
            sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

            # read first line output:[cnt1 , cnt2 , avg10 , uS/h]
            print(ser.readline())

            # run loop
            while True:
                data = sio.readline()
                time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
                if data:
                    data_to_stream = time + ', ' + data
                    stream.write(data_to_stream)
                    print(data_to_stream)
                    data, time, data_to_stream = None, None, None
