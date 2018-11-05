# i2c_interface.py
# Functions responsible for reading i2c from the RPi.
from scipy.constants.constants import g
import smbus


class I2CDevice:
    address = None

    def __init__(self, device_number):
        self.address = get_address(device_number)


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
        device = I2CDevice(device_number)  # Initialize device
        self.bus.write_byte_data(device_address, 0x2A, 1)  # Initialize control register
        self.device_dict[device_number] = device  # Add device to dict

    def get_device(self, device_number):
        """ Returns the specified I2C device object. """
        if device_number not in self.device_dict.keys():
            raise ValueError("Out of bounds device number:", device_number)
        return self.device_dict[device_number]

    def read_device(self, device_number):
        """ Reads the specified device and returns its raw data. """
        device = self.get_device(device_number)
        # TODO Finish implementing this method
        return self.bus.read_i2c_block_data(device.address, 0x01, 6)


def get_address(device_number):
    if device_number == 0:
        return 0x1C
    elif device_number == 1:
        return 0x1D
    else:
        raise ValueError("Bad device number:", device_number)


if __name__ == "__main__":
    pass
