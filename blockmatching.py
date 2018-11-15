#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:23:00 2018

@author: brendanpaver
"""
import numpy as np
import matplotlib.pyplot as plt
def TDOA(accel_0,accel_1,timearray):
    # Number of indices between the correlation
    #accel_0 = []
    #accel_1 = []
    #timeArray = []
    #for i in range (0,50):
        #accel_0.append(np.sin(i))
        #accel_1.append(np.sin(i+3))
        #timeArray.append(i)
    corr = np.correlate(accel_0,accel_1, "same")
    #print(corr)
    #indexShift = -100
    #print(corr.size)
    for j in range (0,corr.size):
        if (corr[j] > indexShift):
            print(corr[j])
            indexShift = j
    plt.plot(timeArray,accel_1,'r')
    plt.plot(timeArray,accel_0,'g')
    plt.show()
    return indexShift

