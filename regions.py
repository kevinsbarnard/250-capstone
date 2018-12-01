# regions.py
# Used to define regions on the board


class Region:
    """ Region to define functionality. """
    top_x = 0
    top_y = 1
    bottom_x = 1
    bottom_y = 0
    action = None

    def __init__(self, top_x, top_y, bottom_x, bottom_y):
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = bottom_x
        self.bottom_y = bottom_y

    def set_action(self, action):
        """ Sets the action to be performed for this region. """
        self.action = action

    def within(self, x, y):
        """ Returns if the given point is within the region's bounds. """
        return x >= self.top_x and x <= self.bottom_x and y >= self.bottom_y and y <= self.top_y
