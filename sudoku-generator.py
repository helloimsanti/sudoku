import pygame, sys


class Sudoku:
    def __init__(self):
        # Screen settings
        self.WIDTH = 900
        self.HEIGHT = 900
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.RUN = True

    def set_bg_color(self) -> None:
        """Sets the background color of the screen."""

        raise NotImplementedError('I\'m still trying to find a cool color.')

    def main(self) -> None:
        """Contains the main loop as well as the
        event rules."""

        while self.RUN:
            for event in pygame.event.get():
                # Leave this here for now.
                if event.type == pygame.QUIT:
                    self.RUN = False


if __name__ == '__main__':
    pygame.init()

    sudoku = Sudoku()
    
    # I'll remove this once I find a color for the background.
    try:
        sudoku.set_bg_color()

    except NotImplementedError as err:
        print(f'[!] {err}')

    sudoku.main()
