#!/usr/bin/env python3

import os, sys
from matplotlib import pyplot as plt
import numpy as np

for file in os.listdir("./logs"):
    if ".csv" in file:
        pass
    else:
        continue
    
    f = os.path.join("./logs", file)
    r = np.genfromtxt(f, delimiter=',')
    
    plt.plot(r[:,0], r[:,4])
    name = os.path.splitext(file)[0]
    plt.savefig(name + '.png', bbox_inches='tight')
    plt.close('all')
# r[:,0] slice the 0th column