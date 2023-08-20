# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ONE = (27, 27, 245)
TWO = (0, 123, 0)
THREE = (243, 33, 33)
FOUR = (1, 1, 123)
FIVE = (124, 2, 2)
SIX = (2, 124, 124)
SEVEN = BLACK
EIGHT = (128, 128, 128)

def get_color(value):
    match value:
        case 1:
            return ONE
        case 2:
            return TWO
        case 3:
            return THREE
        case 4:
            return FOUR
        case 5:
            return FIVE
        case 6:
            return SIX
        case 7:
            return SEVEN
        case _:
            return EIGHT