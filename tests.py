# tests.py
# Tests for program functionality.
import i2c_interface
import hyperbolic_location
import numpy as np
import time
import matplotlib.pyplot as plt


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
    while time.time() - ti < 10:
        acc0.read()
        acc1.read()
        acc2.read()
    print("done")

    acc0_data_z = np.array(list(map(i2c_interface.convert_datum, acc0.get_axis_data(2))))
    acc0_sample_times = np.array(acc0.get_sample_times()) - ti
    plt.plot(acc0_sample_times, acc0_data_z)
    plt.show()


def test_locate():
    """ Tests TDOA target location algorithm. """
    x, y = hyperbolic_location.locate(-.290955, -.08254229)
    print(x, y)


if __name__ == "__main__":
    # test_i2c()
    test_locate()
