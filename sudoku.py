import pygame

from sudoku_generator import *
from board import *


if __name__ == '__main__':
    # sudoku_gen = SudokuGenerator()
    board = Board()

    # I'll leave the background color white for now
    # unless you guys want to change it.
    board.SCREEN.fill((255, 255, 255))
    pygame.display.update()

    run = True

    while run:
        board.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
