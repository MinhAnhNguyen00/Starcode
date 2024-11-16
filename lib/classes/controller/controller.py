from typing import TypeVar

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

        print("Created game instance with type: " + game_instance.g_type.value)
        print("Created gui instance with corresponding game type: " + gui_instance.game.g_type.value)

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
