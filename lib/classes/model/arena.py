import random
from typing import Any

import numpy as np
from numpy import ndarray

from lib.classes.model.direction import Direction
from lib.classes.model.snake_arena_field_types import FieldType


class SnakeArena:
    """
    SnakeArena class. Represents the current arena state of game 'Snake'.
    """

    arena_arr: np.ndarray
    snake_direction: Direction
    snake_head_position: tuple
    snake_body: list
    food_position: tuple

    def __init__(self):
        """
        Initializes the arena for a new game.
        """

        # create empty arena
        arena = np.full((10, 10), FieldType.EMPTY)

        # place snake head randomly
        arena, self.snake_head_position = self.place_element_randomly(arena, FieldType.PLAYER_HEAD)

        # append head to snake body list
        self.snake_body = [self.snake_head_position]

        # place food randomly
        self.arena_arr, self.food_position = self.place_element_randomly(arena, FieldType.FOOD)

        # set the initial orientation of the snake
        self.snake_direction = Direction.RIGHT

    @staticmethod
    def place_element_randomly(arena: np.ndarray, elem_type: FieldType) -> tuple[ndarray, Any] | tuple[ndarray, None]:
        """
        Places an element randomly onto the arena.
        :param arena: the arena to place the element in
        :param elem_type: the type of element to place
        :return: tuple containing the updated arena and the position of the placed element
        """

        # get empty fields (indices of rows and columns)
        empty_fields = np.where(arena == FieldType.EMPTY)

        # combine row and column indices into a list of coordinates
        empty_positions = list(zip(empty_fields[0], empty_fields[1]))

        # select a random position
        if empty_positions:  # ensure there are empty fields available

            # choose random location
            pos = random.choice(empty_positions)

            # place the element in the arena
            arena[pos] = elem_type

            return arena, pos

        # if no empty fields are available, return the arena unchanged and None as position
        return arena, None
