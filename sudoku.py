import pygame

from sudoku_generator import *
from board import *


if __name__ == '__main__':
    # sudoku_gen = SudokuGenerator()
    board = Board()

    board.SCREEN.fill((255, 255, 255))
    pygame.display.update()

    run = True

    while run:
        board.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
