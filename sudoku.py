import pygame

from sudoku_generator import *
from board import *


if __name__ == '__main__':
    # sudoku_gen = SudokuGenerator()
    # clock = pygame.time.Clock()
    board = Board()

    # I'll leave the background color white for now
    # unless you guys want to change it.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        board.SCREEN.fill(board.COLOR)

        board.draw()
        board.select()

        pygame.display.update()
        # clock.tick(60)
