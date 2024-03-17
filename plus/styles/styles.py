from enum import Enum
import reflex as rx

# Constants
MAX_WIDTH="1000px"
MIN_WIDTH="400px"

# Sizes

class EMSize(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.9em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    BIGGER = "4em"

class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    MEDIUM="3"
    DEFAULT = "4"
    LARGE = "6"
    BIG = "7"
    BIGGER = "8"
    VERY_BIG = "9"


class Color(Enum):
    TITLE = "#1e2125"
    TEXT = "#505050"
    PRIMARY = "#2ECCFA"
    SECONDARY = "#BBC3C6"


