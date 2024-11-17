import time
from typing import TypeVar

from pynput.keyboard import Listener

from lib.classes.factory.factory import GuiFactory, GameFactory
from lib.classes.model.game import BaseGame
from lib.classes.model.game_type import GameType
from lib.classes.view.gui import BaseGui

# define generic for game type
B = TypeVar('B', bound=BaseGame)
G = TypeVar('G', bound=BaseGui)


class GameController:

    def __init__(self):
        self.games = []
        self.guis = []

    def start_game(self, g_type: GameType):
        # TODO:
        #   - create game and gui instance
        #   - add instances to collections
        #   - start game loop

        game_instance = GameFactory.build(g_type)
        gui_instance = GuiFactory.build(game_instance)

        self.games.append(game_instance)
        self.guis.append(gui_instance)

        if g_type == GameType.SNAKE:
            self.run_snake_game_loop(game_instance, gui_instance)
        elif g_type == GameType.HANGMAN:
            self.run_hangman_game_loop()
        else:
            raise ValueError(f'Unknown game type: {g_type}')

    def run_snake_game_loop(self, game: B, gui: G):
        """
        Runs the snake game loop.
        :param game: snake game instance
        :param gui: snake gui instance
        """

        # capture keyboard inputs for movement
        listener = Listener(on_press=game.on_key_press)
        listener.start()

        # display initial game state
        gui.visualize_game_state()

        # main game loop
        while not game.is_game_finished():
            # play last buffered move
            game.play_move()
            # update GUI
            gui.visualize_game_state()
            # wait until next game state update
            time.sleep(1)

    def run_hangman_game_loop(self):
        pass

    def get_game_instance_by_type(self, g_type: GameType) -> B | None:
        """
        Returns the game instance corresponding to the given game type.
        :param g_type: Game type of wanted Game instance
        :return: Game instance corresponding to the given game type or None if no game instance exists.
        """

        for game_instance in self.games:
            if game_instance.g_type == g_type:
                return game_instance

        return None

    def get_gui_instance_by_game(self, game: BaseGame) -> G | None:
        """
        Returns the gui instance corresponding to the given game instance.
        :param game: Game instance
        :return: Gui instance corresponding to the given game instance.
        """

        for gui_instance in self.guis:
            if gui_instance.game == game:
                return gui_instance

        return None
