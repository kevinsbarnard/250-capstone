# main.py
# Main application to run
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import i2c_interface
import blockmatching
import hyperbolic_location
import time
from regions import Region

app_states = {
    0: "INFO",
    1: "WARNING",
    2: "ERROR"
}

button_pin = 24

accs = []
regions = []

def setup():
    """ Sets up application. """
    log("Setting up")
    GPIO.setmode(GPIO.BCM)

    # Set up button, pull down internal resistor
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Init bus 0 devices
    bus0 = i2c_interface.I2CBus(0)
    bus0.init_device(1)

    # Init bus 1 devices
    bus1 = i2c_interface.I2CBus(1)
    bus1.init_device(0)
    bus1.init_device(1)

    # Sets up accs list
    accs.clear()
    accs[0] = i2c_interface.Accelerometer(bus1.get_device(0))
    accs[1] = i2c_interface.Accelerometer(bus1.get_device(1))
    accs[2] = i2c_interface.Accelerometer(bus0.get_device(1))

    # Create regions
    for y in range(4):
        for x in range(4):
            regions.append(Region(x/4, (y+1)/4, (x+1)/4, y))

    # Map actions
    regions[0].set_action('0')
    regions[1].set_action('+')
    regions[2].set_action('-')
    regions[3].set_action('Enter')
    regions[4].set_action('1')
    regions[5].set_action('2')
    regions[6].set_action('3')
    regions[7].set_action('Del')
    regions[8].set_action('4')
    regions[9].set_action('5')
    regions[10].set_action('6')
    regions[11].set_action('/')
    regions[12].set_action('7')
    regions[13].set_action('8')
    regions[14].set_action('9')
    regions[15].set_action('*')


def main():
    user_input = ""
    end = False
    while not end:
        t_start = time.time()
        recorded = False

        # Clear accelerometers
        for acc in accs:
            acc.clear()

        # Loop while button is held down
        while GPIO.input(button_pin) == 1:
            # Update flags
            if not recorded:
                recorded = True

            # Read in values
            for acc in accs:
                acc.read()

        # If recorded, retrieve and process data for this instance
        if recorded:
            data = []
            times = []

            # Retrieve data and times
            for acc in accs:
                data.append(acc.get_magnitude_data())
                times.append(acc.get_sample_times())

            # Calculate TDOAs
            tdoa_right = blockmatching.TDOA(data[1], data[0], times[0])
            tdoa_up = blockmatching.TDOA(data[2], data[0], times[0])

            # Calculate point
            x, y = hyperbolic_location.locate(tdoa_right, tdoa_up)

            log("Calculated point = ({}, {})".format(x, y))

            # Make and display plot of detected point
            plt.plot([x], [y], 'o')
            plt.axis([0, 1, 0, 1])
            plt.title("Detected point")
            plt.axes().set_aspect('equal')
            plt.xlabel('x (m)')
            plt.ylabel('y (m)')
            plt.show()

            # Check and process regions
            for region in regions:
                if region.within(x, y):
                    if region.action == 'Enter':
                        end = True  # End loop
                    elif region.action == 'Del':
                        user_input = user_input[:-1]  # Delete last character
                    else:
                        user_input += region.action  # Add action

    # Evaluate and output user input
    print(user_input, '=', eval(user_input))


def cleanup():
    """ Cleans up application. """
    log("Cleaning up")
    GPIO.cleanup()


def log(message, state=0):
    print("[{}]".format(app_states[state]), message)


if __name__ == '__main__':
    setup()
    try:
        main()
    except:
        log("Error in main application execution", 2)
    finally:
        cleanup()
    log("Finished")
