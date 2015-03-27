#!/usr/bin/env python3

line = "TS:1427416884875	Drop:0	RX:251	TX:02403	RSSI:-61.50	    CRC	Data:"

output = line.split('\t')
for x in range(0,5):
    data = output[x]
    if ':' in data and ~(data.find(':') == (len(data)-1)) :
        print(data.split(':')[1])