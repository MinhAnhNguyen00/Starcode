import time

from abc import ABC, abstractmethod
from typing import List
from pynput.keyboard import Key, Listener

from lib.classes.model.arena import SnakeArena
from lib.classes.model.direction import Direction
from lib.classes.model.game_type import GameType
from lib.classes.model.snake_arena_field_types import FieldType


class BaseGame(ABC):
    """
    Abstract base class for games.
    """

    g_type: GameType
    finished: bool

    def __init__(self, g_type: GameType):
        self.g_type = g_type
        self.finished = False

    @abstractmethod
    def play_move(self, **kwargs) -> bool:
        """
        Plays a given move if move is valid according to the game type.
        :param kwargs: move for certain game type
        :return: True if move is valid and was played, False otherwise.
        """
        pass

    @abstractmethod
    def run_game(self):
        """
        Runs the game until game ends.
        """
        pass

    @abstractmethod
    def is_game_finished(self) -> bool:
        """
        Checks if game is finished during last turn.
        """
        pass


class HangmanGame(BaseGame):
    """
    HangmanGame class. Implements the game logic of the game 'Hangman'.
    """

    target_word: str
    player_guesses: List[str]
    turn_count: int
    player_won: bool

    def __init__(self, g_type: GameType):
        super().__init__(g_type)
        self.target_word = self.get_target_word()
        self.player_guesses = []
        self.turn_count = 0
        self.player_won = False

    def run_game(self):
        pass

    @staticmethod
    def get_target_word() -> str:
        """
        Loads a random word from the words list located at msc/words.txt. The word should be upper case...
        TODO: implement!!!
        """
        return "WORD"

    def play_move(self, guess: str) -> bool:
        """
        Plays a move during hangman game.
        :param guess: guess of the player.
        :return: True if the given guess character was valid, False otherwise.

        TODO: implement!!!
        """
        print("This is the original backend implementation...")
        return False

    def is_game_finished(self) -> bool:
        """
        Checks if the game is finished or not. Sets the finished flag and checks if the player has won.
        TODO: implement!!!
        """
        pass


class SnakeGame(BaseGame):
    """
    SnakeGame class. Implements the game logic of the game 'Snake'.
    """

    # class member
    player_score: int
    arena: SnakeArena

    def __init__(self, g_type: GameType):
        super().__init__(g_type)
        self.player_score = 0
        self.arena = SnakeArena()

    def run_game(self):
        """
        Runs the game until player loses.
        """
        listener = Listener(on_press=self.on_key_press)
        listener.start()  # start listening to keyboard input

        while not self.is_game_finished():
            self.play_move()
            time.sleep(0.2)  # control game speed

        listener.stop()  # stop listening when the game ends
        print("Game Over! Your score:", self.player_score)

    def play_move(self):
        """
        Plays a move during snake game. It takes the last buffered move as input.
        """

        head = self.arena.snake_body[-1]

        if self.arena.snake_direction == Direction.UP:
            new_head = (head[0] - 1, head[1])
        elif self.arena.snake_direction == Direction.DOWN:
            new_head = (head[0] + 1, head[1])
        elif self.arena.snake_direction == Direction.LEFT:
            new_head = (head[0], head[1] - 1)
        elif self.arena.snake_direction == Direction.RIGHT:
            new_head = (head[0], head[1] + 1)
        else:
            return

        # check for collisions
        if (
            new_head in self.arena.snake_body  # collision with itself
            or new_head[0] < 0
            or new_head[1] < 0
            or new_head[0] >= self.arena.arena_arr.size
            or new_head[1] >= self.arena.arena_arr.size  # collision with walls
        ):
            self.finished = True
            return

        # move the snake
        self.arena.snake_body.append(new_head)
        if new_head == self.arena.food_position:
            self.player_score += 1
            self.arena.arena_arr, self.arena.food_position = self.arena.place_element_randomly(self.arena.arena_arr,
                                                                                               FieldType.FOOD)
        else:
            self.arena.snake_body.pop(0)  # remove the tail unless food is eaten

    def is_game_finished(self) -> bool:
        """
        Checks if the game is finished or not.
        """
        return self.finished

    def on_key_press(self, key):
        """
        Updates the direction based on keyboard input.
        """

        try:
            current_direction = self.arena.snake_direction  # current direction of the snake

            # prevent moving in the opposite direction
            if key == Key.up and current_direction != Direction.DOWN:
                self.arena.snake_direction = Direction.UP
            elif key == Key.down and current_direction != Direction.UP:
                self.arena.snake_direction = Direction.DOWN
            elif key == Key.left and current_direction != Direction.RIGHT:
                self.arena.snake_direction = Direction.LEFT
            elif key == Key.right and current_direction != Direction.LEFT:
                self.arena.snake_direction = Direction.RIGHT

        # if none of the conditions above are met, the direction remains unchanged
        except AttributeError:
            pass
