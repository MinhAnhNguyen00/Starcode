from typing import List

from IPython.core.display_functions import display, clear_output
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Circle, Rectangle


class HangmanGui:

    def __init__(self, target: List, masked_target: List, player_lives: int = 10):
        # Initial member creation
        # plot for gui render
        self.fig, self.ax = plt.subplots()
        # target representation
        self.target = target
        self.masked_target = masked_target
        # set player lives and error count
        self.player_lives = player_lives
        self.player_error_count = 10 - player_lives
        self.covered_letters = []
        self.failed_letters = []

        # Notification box text
        self.notification_message = "Willkommen zu Hangman!\nBitte gib deinen Namen ein..."

        # Define mapping for error counts and drawing functions
        self.error_steps = [
            self.draw_base,
            self.draw_pillar,
            self.draw_beam,
            self.draw_rope,
            self.draw_head,
            self.draw_body,
            self.draw_left_arm,
            self.draw_right_arm,
            self.draw_left_leg,
            self.draw_right_leg
        ]

        # Plot initial game state
        self.ax.set_xlim(-2, 6)  # Extend the x-axis to accommodate the notification box
        self.ax.set_ylim(-2, 5)
        self.ax.axis('off')
        self.ax.set_aspect('equal')

        self.display_welcome()

    def update(self, masked_target: List, player_error_count: int, failed_chars: List[str], message: str = None):
        self.masked_target = masked_target
        self.player_error_count = player_error_count
        self.covered_letters = set(failed_chars)
        if message is not None:
            self.notification_message = message

    def display_welcome(self):
        self.display_notification_box()
        clear_output(wait=True)
        display(self.fig)
        plt.close(self.fig)
        name = input("Enter your name: ")
        self.clear_render()
        self.update_notification_box(f"Welcome, {name}!\nLet's play hangman!")
        self.cycle(self.masked_target, self.player_lives, self.failed_letters)

    def display(self):
        # Reset plot
        self.clear_render()
        # Display masked word
        self.display_masked_word()
        # Draw hangman figure for given error count
        for i in range(self.player_error_count):
            self.error_steps[i]()
        # Display notification box
        self.display_notification_box()
        clear_output(wait=True)
        display(self.fig)
        # Close the figure to avoid duplicate rendering
        plt.close(self.fig)

    def cycle(self, masked_target: List, player_lives: int, failed_chars: List[str], message: str = None):
        self.update(masked_target, 10 - player_lives, failed_chars, message)
        self.display()

    def display_masked_word(self):
        masked_word = " ".join(self.masked_target)
        self.ax.text(2.5, 2.5, masked_word, fontsize=20, ha='left', va='center')
        guessed_letters = ", ".join(sorted(self.covered_letters))
        self.ax.text(2.5, 1.75, f"Fehlgeschlagene Buchstaben: {guessed_letters}", fontsize=12, ha='left', va='center')

    def display_notification_box(self):
        self.ax.text(10, 2.0, self.notification_message, fontsize=20, ha='left', va='center')

    def update_notification_box(self, message: str):
        self.notification_message = message
        self.display_notification_box()
        clear_output(wait=True)
        display(self.fig)
        plt.close(self.fig)

    def clear_render(self):
        self.ax.cla()
        self.ax.axis('off')
        self.ax.set_xlim(-2, 6)  # Extend the x-axis to accommodate the notification box
        self.ax.set_ylim(-2, 5)
        self.ax.set_aspect('equal')

    def draw_base(self):
        self.ax.add_line(Line2D([-1, 1], [-2, -2], linewidth=3, color='black'))

    def draw_pillar(self):
        self.ax.add_line(Line2D([0, 0], [-2, 4], linewidth=3, color='black'))

    def draw_beam(self):
        self.ax.add_line(Line2D([0, 1], [4, 4], linewidth=3, color='black'))

    def draw_rope(self):
        self.ax.add_line(Line2D([1, 1], [4, 3.2], linewidth=3, color='black'))

    # Resized figure components
    def draw_head(self):
        self.ax.add_patch(
            Circle((1, 2.8), 0.4, fill=False, color='black', linewidth=3))

    def draw_body(self):
        self.ax.add_line(Line2D([1, 1], [2.4, 1], linewidth=3, color='black'))

    def draw_left_arm(self):
        self.ax.add_line(Line2D([1, 0.3], [2.3, 1.8], linewidth=3, color='black'))

    def draw_right_arm(self):
        self.ax.add_line(Line2D([1, 1.7], [2.3, 1.8], linewidth=3, color='black'))

    def draw_left_leg(self):
        self.ax.add_line(Line2D([1, 0.5], [1, 0.2], linewidth=3, color='black'))

    def draw_right_leg(self):
        self.ax.add_line(Line2D([1, 1.5], [1, 0.2], linewidth=3, color='black'))

