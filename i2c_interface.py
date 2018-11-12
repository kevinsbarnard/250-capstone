# i2c_interface.py
# Functions responsible for reading i2c from the RPi.
from scipy.constants.constants import g
import smbus
import time

class Accelerometer:
    device = None
    sample_times = []
    sample_data = [[], [], []]

    def __init__(self, device):
        self.device = device

    def read(self):
        """ Returns a sample time and len=3 list of read accelerometer data. """
        read_time = time.time()
        read_data = self.normalize_data(self.device.read())
        self.sample_times.append(read_time)
        for i in range(3):
            self.sample_data[i].append(read_data[i])
        return read_time, read_data

    def get_sample_times(self):
        return self.sample_times

    def get_axis_data(self, axis):
        if axis in range(3):
            return self.sample_data[axis]
        else:
            raise ValueError("Bad axis:", axis)


class I2CDevice:
    address = None
    bus = None

    def __init__(self, bus, device_number):
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


def normalize_data(self, raw_data):
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


def convert_datum(self, datum):
    """ Converts normalized data list to acceleration data (m/s^2). """
    return datum * 9.81 / 1024


def get_address(device_number):
    if device_number == 0:
        return 0x1C
    elif device_number == 1:
        return 0x1D
    else:
        raise ValueError("Bad device number:", device_number)


if __name__ == "__main__":
    pass
