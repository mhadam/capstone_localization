#!/usr/bin/env python3

'''
This script must run above a folder named "logs"

'''

import sys, re, time, os

def convert(tf):
    write = sys.stdout.write
    number = 'none'
    txNumber = re.compile("(?<=TX:)(\d{5})")
    nodes = set()
    
    f = open(tf)

    for line in f:
        if "TX:" in line:
            txNum = txNumber.search(line).groups()[0]
            if txNum not in nodes:
                nodes.add(txNum)
            print(nodes)
            print(line)

    f.seek(0)
    f.tell()
    time.sleep(5)

    for tx in nodes:
        f.seek(0)
        tf2 = 'log_' + 'TX' + tx + '.txt'
        f2 = open(tf2, "w")
        for line in f:
            if ("TX:" + tx) not in line:
                continue
            else:
                f2.write(line)
        f2.close()
        
    f.close()

for file in os.listdir("./logs"):
    if file.endswith(".txt"):
        convert(os.path.join("./logs", file))
