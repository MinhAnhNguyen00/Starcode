from enum import Enum


class FieldType(Enum):
    EMPTY = 0,
    PLAYER_BODY = 1,
    PLAYER_HEAD = 2,
    FOOD = 3


class FieldColor(Enum):
    WHITE = "white"
    GREEN = "green"
    BLACK = "black"
    RED = "red"
