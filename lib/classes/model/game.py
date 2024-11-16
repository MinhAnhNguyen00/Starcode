from abc import ABC, abstractmethod
from typing import List

from lib.classes.model.arena import SnakeArena
from lib.classes.model.game_type import GameType


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

    def play_move(self, move: str):
        """
        Plays a move during snake game. Takes keyboard arrows as input.
        TODO: implement!!!
        """

    def is_game_finished(self) -> bool:
        """
        Checks if the game is finished or not.
        TODO: implement!!!
        """
        pass
