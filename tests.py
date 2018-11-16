# tests.py
# Tests for program functionality.
import i2c_interface
import hyperbolic_location
import numpy as np
import time
import matplotlib.pyplot as plt
import blockmatching


def test_i2c():
    """ Tests basic I2C interfacing functionality on all buses/addresses. """

    bus0 = i2c_interface.I2CBus(0)
    bus1 = i2c_interface.I2CBus(1)

    bus1.init_device(0)
    bus1.init_device(1)
    bus0.init_device(1)

    acc0 = i2c_interface.Accelerometer(bus1.get_device(0))
    acc1 = i2c_interface.Accelerometer(bus1.get_device(1))
    acc2 = i2c_interface.Accelerometer(bus0.get_device(1))

    ti = time.time()
    print("Reading data...")
    while time.time() - ti < 5:
        acc0.read()
        acc1.read()
        acc2.read()
    print("done")

    acc0_sample_times = np.array(acc0.get_sample_times()) - ti
    acc0_magnitudes = acc0.get_magnitude_data()
    acc1_sample_times = np.array(acc1.get_sample_times()) - ti
    acc1_magnitudes = acc1.get_magnitude_data()
    acc2_sample_times = np.array(acc2.get_sample_times()) - ti
    acc2_magnitudes = acc2.get_magnitude_data()
    
    plt.plot(acc0_sample_times, acc0_magnitudes, label='acc0')
    plt.plot(acc1_sample_times, acc1_magnitudes, label='acc1')
    plt.plot(acc2_sample_times, acc2_magnitudes, label='acc2')
    plt.legend()
    plt.show()

    tdoa10 = blockmatching.TDOA(acc1_magnitudes, acc0_magnitudes, acc0_sample_times)
    tdoa20 = blockmatching.TDOA(acc2_magnitudes, acc0_magnitudes, acc0_sample_times)
    print(tdoa10, tdoa20)


def test_locate():
    """ Tests TDOA target location algorithm. """
    x, y = hyperbolic_location.locate(-.290955, -.08254229)
    print(x, y)


if __name__ == "__main__":
    test_i2c()
    # test_locate()
