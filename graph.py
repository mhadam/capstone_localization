#!/usr/bin/env python3

import os, sys, time
from matplotlib import pyplot as plt
import numpy as np

for file in os.listdir("./logs"):
    if ".csv" in file:
        pass
    else:
        continue
    
    f = os.path.join("./logs", file)
    r = np.genfromtxt(f, delimiter=',')
    print(r)
    
    g = [row for row in r if (row[3] == 2403) and (row[2] == 251)]
    g = np.array(g)
    
    plt.plot(g[:,0], g[:,4])
    name = os.path.splitext(file)[0]
    plt.savefig(name + '.png', bbox_inches='tight')
    plt.close('all')
# r[:,0] slice the 0th column