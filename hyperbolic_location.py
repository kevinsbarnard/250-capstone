# hyperbolic_location.py
# Performs hyperbolic location to find points given Time Difference of Arrivals (TDOA).
import math


def locate(k1, k2):
    """ Calculates and returns the 0-1 normalized (x, y) tuple given two TDOAs """
    x = (-1 + k2 ** 2 - k1 ** 2 * (-1 + k2 ** 2) + k1 * k2 * (-1 + k2 ** 2) - math.sqrt(
        -k1 ** 2 * (-1 + k1 ** 2) * (-1 + k2 ** 2) * (-2 + k1 ** 2 - 2 * k1 * k2 + k2 ** 2))) / (
                    2 * (-1 + k1 ** 2 + k2 ** 2))
    y = -((k1 + k1 ** 2 * k2 - k1 ** 4 * k2 - k1 * k2 ** 2 + k1 ** 3 * (-1 + k2 ** 2) + k2 * math.sqrt(
        -k1 ** 2 * (-1 + k1 ** 2) * (-1 + k2 ** 2) * (-2 + k1 ** 2 - 2 * k1 * k2 + k2 ** 2))) / (
                      2 * k1 * (-1 + k1 ** 2 + k2 ** 2)))
    return x, y
