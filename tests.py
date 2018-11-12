# tests.py
# Tests for program functionality.
from i2c_interface import *
import numpy as np
import matplotlib.pyplot as plt


def test_i2c():
    bus0 = I2CBus(0)
    bus1 = I2CBus(1)

    bus1.init_device(0)
    bus1.init_device(1)
    bus0.init_device(0)

    acc0 = Accelerometer(bus1.get_device(0))
    acc1 = Accelerometer(bus1.get_device(1))
    acc2 = Accelerometer(bus0.get_device(0))

    ti = time.time()
    while time.time() - ti < 10:
        acc0.read()
        acc1.read()
        acc2.read()

    acc0_data_z = np.array(map(convert_datum, acc0.get_axis_data(2)))
    acc0_sample_times = np.array(acc0.get_sample_times())
    plt.plot(acc0_sample_times, acc0_data_z)
    plt.show()


if __name__ == "__main__":
    pass
