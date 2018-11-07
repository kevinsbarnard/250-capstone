# tests.py
# Tests for program functionality.
import i2c_interface


def test_i2c():
    bus0 = I2CBus(0)
    bus1 = I2CBus(1)
    bus0.init_device(0)
    bus0.init_device(1)
    bus1.init_device(0)
    acc0 = bus0.get_device(0)
    acc1 = bus0.get_device(1)
    acc2 = bus1.get_device(2)

if __name__ == "__main__":
    pass
