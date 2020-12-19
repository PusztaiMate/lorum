from enum import Enum


class BadRankException(Exception):
    pass


class Rank(Enum):
    UNKNOWN_RANK = "UNKNOWN_RANK"
    VII = "VII"
    VIII = "VIII"
    IX = "IX"
    X = "X"
    UNDER = "UNDER"
    UPPER = "UPPER"
    KING = "KING"
    ACE = "ACE"
