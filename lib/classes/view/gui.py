from abc import ABC
from typing import TypeVar
from matplotlib.colors import to_rgb
from IPython.display import clear_output, display

import numpy as np
import matplotlib.pyplot as plt

from lib.classes.model.game import BaseGame, HangmanGame, SnakeGame
from lib.classes.model.snake_arena_field_types import FieldColor, FieldType

# define generic for game type
T = TypeVar('T', bound=BaseGame)


class BaseGui(ABC):
    game: T

    def __init__(self, game: BaseGame):
        self.game = game


class HangmanGui(BaseGui):
    def __init__(self, game: HangmanGame):
        super().__init__(game)


class SnakeGui(BaseGui):
    def __init__(self, game: SnakeGame):
        super().__init__(game)

    def visualize_game_state(self):
        """
        visualize the game state using matplotlib.
        """

        # clear the previous output
        clear_output(wait=True)

        # map field types to rgb values
        field_to_rgb = {
            FieldType.EMPTY: to_rgb("white"),
            FieldType.PLAYER_BODY: to_rgb("darkgreen"),
            FieldType.PLAYER_HEAD: to_rgb("green"),
            FieldType.FOOD: to_rgb("red"),
        }

        # create an rgb arena array
        rgb_arena = np.zeros((*self.game.arena.arena_arr.shape, 3))  # shape: (rows, cols, 3)

        # replace field types with rgb values in the arena
        for field_type, rgb_value in field_to_rgb.items():
            mask = self.game.arena.arena_arr == field_type
            rgb_arena[mask] = rgb_value

        # render the game state using matplotlib
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(rgb_arena, aspect="equal")

        # remove axis labels
        ax.set_xticks([])
        ax.set_yticks([])

        display(fig)
        plt.close(fig)
