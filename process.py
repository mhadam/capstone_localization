#!/usr/bin/env python3

'''
This script must run above a folder named "logs"

'''

import sys, re, time, os
import numpy as np

def parse(f):
    path, filename = os.path.split(f)
    ymd, hm = os.path.splitext(filename)[0].split("-")
    
    return ymd, hm

def convert(tf): # feed it the full file path
    write = sys.stdout.write
    number = 'none'
    txNumber = re.compile("(?<=TX:)(\d{5})")
    nodes = set()
    
    f = open(tf)
    num_lines = sum(1 for line in f)
    f.seek(0) # seek back to beginning of file

    new_array = []

    #process each line of the log
    for line in f:
        if "TX:" in line:
            pass
        else:
            continue
        newline = []
        output = line.split('\t')
        for x in range(0,5): # extract each datum
            data = output[x]
            if ':' in data and ~(data.find(':') == (len(data)-1)): # discard the useless stuff (CRC/"data" field)
                if '.' in data:
                    newline.append(np.float(data.split(':')[1]))
                else:
                    newline.append(np.int32(data.split(':')[1]))
        new_array.append(newline)
        
    f.close()
    
    return new_array # returns regular python array

for file in os.listdir("./logs"):
    if ".csv" in file:
        continue
    
    tf = os.path.join("./logs", file)
    
    final_array = np.array(convert(tf))
    
    ymd, hm = parse(tf) # remove file ext. and separate into date and time
    print(ymd, hm)
    print(final_array)
    
    new_filename = ymd + '-' + hm + ".csv"
    new_filepath = os.path.join("./logs", new_filename)
    np.savetxt(new_filepath, final_array, delimiter=",")
    
    #if not os.path.exists(): os.makedirs(newpath)
    #if file.endswith(".txt"):
        #convert(os.path.join("./logs", file))