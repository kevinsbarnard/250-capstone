#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:23:00 2018

@author: brendanpaver
"""
import numpy as np
import matplotlib.pyplot as plt

def TDOA(accel_0, accel_1, timeArray):
    corr = np.correlate(accel_0,accel_1, "same")
    max_index = np.argmax(corr)
    print("max_index =", max_index)
    avg_diff = np.mean(np.ediff1d(timeArray))
    print("avg_diff =", avg_diff)
    return avg_diff * max_index

if __name__ == "__main__":
    print(TDOA(accel_0,accel_1,timeArray))
