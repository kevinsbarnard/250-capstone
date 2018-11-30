# i2c_interface.py
# Functions responsible for reading i2c from the RPi.
import smbus
import time
import numpy as np


class Accelerometer:
    device = None
    sample_times = None
    sample_data = None

    def __init__(self, device):
        self.device = device
        self.clear()

    def read(self):
        """ Returns a sample time and len=3 list of read accelerometer data. """
        read_time = time.time()
        read_data = normalize_data(self.device.read())
        self.sample_times.append(read_time)
        for i in range(3):
            self.sample_data[i].append(read_data[i])
        return read_time, read_data

    def clear(self):
        """ Clears sample times and sample data lists. """
        self.sample_times = []
        self.sample_data = [[], [], []]

    def get_sample_times(self):
        """ Returns a numpy array of the recorded sample times. """
        return np.array(self.sample_times)

    def get_axis_data(self, axis):
        """ Returns a numpy array of the data collected for a given axis.
        0 = x
        1 = y
        2 = z
        """
        if axis in range(3):
            return np.array(self.sample_data[axis])
        else:
            raise ValueError("Bad axis:", axis)

    def get_magnitude_data(self):
        """ Performs a vectorized calculation and returns a numpy array of the magnitude data. """
        x = self.get_axis_data(0)
        y = self.get_axis_data(1)
        z = self.get_axis_data(2)
        return np.sqrt(x**2 + y**2 + z**2)


class I2CDevice:
    address = None
    bus = None

    def __init__(self, bus, device_number):
        self.bus = bus
        self.address = get_address(device_number)

    def read(self):
        """ Reads and returns a list of raw register data. """
        return self.bus.read_i2c_block_data(self.address, 0x01, 6)


class I2CBus:
    port = 0
    bus = None
    device_dict = {}

    def __init__(self, port):
        self.port = port
        self.bus = smbus.SMBus(port)

    def init_device(self, device_number):
        """ Initializes an I2C device and adds it to device_dict. """
        device_address = get_address(device_number)
        device = I2CDevice(self, device_number)  # Initialize device
        self.bus.write_byte_data(device_address, 0x2A, 1)  # Initialize control register
        self.device_dict[device_number] = device  # Add device to dict

    def get_device(self, device_number):
        """ Returns the specified I2C device object. """
        if device_number not in self.device_dict.keys():
            raise ValueError("Out of bounds device number:", device_number)
        return self.device_dict[device_number]

    def read_i2c_block_data(self, address, reg_start, num_regs):
        return self.bus.read_i2c_block_data(address, reg_start, num_regs)


def normalize_data(raw_data):
    """ Converts raw accelerometer data to normalized values. """
    data = [0, 0, 0]

    # Convert to numbers
    data[0] = (raw_data[0] << 4) + (raw_data[1] >> 4)
    data[1] = (raw_data[2] << 4) + (raw_data[3] >> 4)
    data[2] = (raw_data[4] << 4) + (raw_data[5] >> 4)

    # Fix 2's complement numbers
    for i in range(3):
        if data[i] >> 11 == 1:
            data[i] -= 2**12

    return data


def convert_datum(datum):
    """ Converts normalized data list to acceleration data (m/s^2). """
    return datum * 9.81 / 1024


def get_address(device_number):
    """ Maps device numbers. """
    if device_number == 0:
        return 0x1C
    elif device_number == 1:
        return 0x1D
    else:
        raise ValueError("Bad device number:", device_number)


if __name__ == "__main__":
    pass
