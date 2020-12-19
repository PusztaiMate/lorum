from enum import Enum


class BadSuitException(Exception):
    pass


class Suit(Enum):
    UNKNOWN_SUIT = "UNKNOWN_SUIT"
    HEARTS = "HEARTS"
    ACORNS = "ACORNS"
    LEAVES = "LEAVES"
    BELLS = "BELLS"