import random

import numpy as np

from lib.classes.model.snake_arena_field_types import FieldType


class SnakeArena:
    """
    SnakeArena class. Represents the current arena state of game 'Snake'.
    """

    arena_arr: np.ndarray

    def __init__(self):
        self.arena_arr = self.initialize_arena()

    def initialize_arena(self):
        """
        Initializes the arena for a new game.
        """

        # create empty arena
        arena = np.full((10, 10), FieldType.EMPTY)

        # place snake head randomly
        arena = self.place_element_randomly(arena, FieldType.PLAYER_HEAD)

        # place food randomly
        arena = self.place_element_randomly(arena, FieldType.FOOD)

        return arena

    @staticmethod
    def place_element_randomly(arena: np.ndarray, elem_type: FieldType) -> np.ndarray:
        """
        Places an element randomly onto the arena.
        :param arena: the arena to place the element in
        :param elem_type: the type of element to place
        :return: arena with newly placed element
        """

        # get empty fields (indices of rows and columns)
        empty_fields = np.where(arena == FieldType.EMPTY)

        # combine row and column indices into a list of coordinates
        empty_positions = list(zip(empty_fields[0], empty_fields[1]))

        # select a random position
        if empty_positions:  # ensure there are empty fields available
            pos = random.choice(empty_positions)

            # place the element in the arena
            arena[pos] = elem_type

        return arena


