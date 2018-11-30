# blockmatching.py
# TDOA calculation
import numpy as np
import matplotlib.pyplot as plt


def TDOA(accel_0, accel_1, timeArray):
    corr = np.correlate(accel_0,accel_1, "same")
    index_offset = np.argmax(corr) - corr.size / 2
    avg_diff = np.mean(np.ediff1d(timeArray))
    return avg_diff * index_offset
