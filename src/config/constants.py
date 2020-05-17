ABOVE = "above"
BELOW = "below"
LEFT = "left"
RIGHT = "right"
DIRECTIONS = [ABOVE, RIGHT, BELOW, LEFT]
MAX_DEPTH = 4
GREEN = 1
YELLOW = 2
RED = 3
TOP_SPOT = 0
LEFT_SPOT = 1
MIDDLE_SPOT = 2
RIGHT_SPOT = 3
BOTTOM_SPOT = 4


def opposite(direction):
    return DIRECTIONS[(DIRECTIONS.index(direction) + 2) % 4]
