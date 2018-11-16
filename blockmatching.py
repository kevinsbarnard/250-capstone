
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:23:00 2018

@author: brendanpaver
"""
import numpy as np
import matplotlib.pyplot as plt

def TDOA(accel_0,accel_1,timeArray):
    
    corr = np.correlate(accel_0,accel_1, "same")
    for j in range (0,corr.size):
        if ( j == 0):
            indexShift = corr[0]
        else:
            if (corr[j] > indexShift):
                indexShift = j
    # Not sure if this is how we want to do time
    timeDiff = timeArray[indexShift] - timeArray[0]
    return timeDiff
print(TDOA(accel_0,accel_1,timeArray))
