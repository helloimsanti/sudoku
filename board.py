from sudoku import start_main

import pygame
import sys


class Board:
    pygame.init()

    def __init__(self, difficulty):
        # Screen settings
        self.COLOR = (216, 255, 236)
        self.WIDTH = 660
        self.HEIGHT = 780
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.ICON = pygame.image.load('images/sudoku-icon.png')
        pygame.display.set_caption('Sudoku')
        pygame.display.set_icon(self.ICON)

        # Sound settings
        self.MOVE_SFX = pygame.mixer.Sound('sfx/movement-blip.mp3')
        self.MOVE_SFX_VOL = 0.4
        self.RESET_SFX = pygame.mixer.Sound('sfx/reset-sfx.mp3')
        self.RESET_SFX_VOL = 0.1

        # Grid settings
        self.SQUARE_SIZE = 220
        self.SUBSQUARE_SIZE = 73
        self.ROWS = 3
        self.COLS = 3
        self.LINE_COLOR = (0, 0, 0)
        self.SUBLINE_COLOR = (64, 64, 64)
        self.LINE_WIDTH = 6
        self.SUBlINE_WIDTH = 2

        # Menu settings
        self.RESTART_COLOR = (51, 255, 153)
        self.RESTART_BORDER_COLOR = (0, 102, 51)
        self.RESET_COLOR = (51, 255, 153)
        self.RESET_BORDER_COLOR = (0, 102, 51)
        self.EXIT_COLOR = (51, 255, 153)
        self.EXIT_BORDER_COLOR = (0, 102, 51)
        self.BUTTON_BORDER_WIDTH = 5
        self.BUTTON_X = 40
        self.BUTTON_Y = 690
        self.BUTTON_WIDTH = 140
        self.BUTTON_HEIGHT = 70
        self.MENU_FONT = 'fonts/MotleyForcesRegular.ttf'
        self.MENU_FONT_SIZE = 34
        self.MENU_FONT_COLOR = (255, 255, 255)

        # Select box settings
        self.SELECT_COLOR = (255, 0, 0)
        self.SELECT_X = 0
        self.SELECT_Y = 0
        self.SELECT_WIDTH = 75
        self.SELECT_HEIGHT = 75
        self.SELECT_BORDER_WIDTH = 4

        # Number settings
        self.NUMBER_FONT = 'fonts/MotleyForcesRegular.ttf'
        self.NUMBER_FONT_SIZE = 40
        self.NUMBER_X = 27
        self.NUMBER_Y = 25

        # Game difficulty
        self.difficulty = difficulty

    def draw(self, board):
        """Draws an outline of the Sudoku grid, with bold
        lines to delineate the 3x3 boxex. It also draws
        every cell on the board."""

        # The board
        board = [[int(x) for x in row] for row in board]

        # Draws smaller vertical lines.
        i = 1

        for sub_row in range(1, self.ROWS * 3):
            pygame.draw.line(self.SCREEN,
                             self.SUBLINE_COLOR,
                             (0, self.SUBSQUARE_SIZE * i),
                             (self.WIDTH, self.SUBSQUARE_SIZE * i),
                             width=self.SUBlINE_WIDTH)

            i += 1

            if i == 3 or i == 6:
                self.SUBlINE_WIDTH = 0
            else:
                self.SUBlINE_WIDTH = 2

        # Draws smaller horizontal lines.
        i = 1

        for sub_col in range(1, self.COLS * 3):
            pygame.draw.line(self.SCREEN,
                             self.SUBLINE_COLOR,
                             (self.SUBSQUARE_SIZE * i, 0),
                             (self.SUBSQUARE_SIZE * i, self.HEIGHT - 120),
                             width=self.SUBlINE_WIDTH)

            i += 1

            if i == 3 or i == 6:
                self.SUBlINE_WIDTH = 0
            else:
                self.SUBlINE_WIDTH = 2

        # Draws vertical lines.
        i = 1

        for row in range(1, self.ROWS + 1):
            pygame.draw.line(self.SCREEN,
                             self.LINE_COLOR,
                             (0, self.SQUARE_SIZE * i),
                             (self.WIDTH, self.SQUARE_SIZE * i),
                             width=self.LINE_WIDTH)

            i += 1

        # Draws horizontal lines.
        i = 1

        for col in range(1, self.COLS):
            pygame.draw.line(self.SCREEN,
                             self.LINE_COLOR,
                             (self.SQUARE_SIZE * i, 0),
                             (self.SQUARE_SIZE * i, self.HEIGHT - 120),
                             width=self.LINE_WIDTH)

            i += 1

        # Draws the bordering vertical lines.
        pygame.draw.line(self.SCREEN, self.LINE_COLOR, (0, 0), (0, self.WIDTH), width=self.LINE_WIDTH)
        pygame.draw.line(self.SCREEN, self.LINE_COLOR, (self.WIDTH, 0), (self.WIDTH, self.HEIGHT), width=self.LINE_WIDTH)

        # Font class for the numbers.
        number_font = pygame.font.Font(self.NUMBER_FONT, self.NUMBER_FONT_SIZE)

        h_spacing = 0
        v_spacing = 0

        # Add the numbers to the Sudoku board.
        for array in board:
            for num in range(len(array)):
                # Add user-inputted numbers.
                if array[num] > 9:
                    number = number_font.render(str(int(array[num] / 10)), True, (0, 102, 0))
                    self.SCREEN.blit(number, (self.NUMBER_X + h_spacing, self.NUMBER_Y + v_spacing))

                    h_spacing += self.SUBSQUARE_SIZE

                    if num == 8:
                        h_spacing = 0
                        v_spacing += self.SUBSQUARE_SIZE

                # Remove zeros
                elif array[num] != 0:
                    number = number_font.render(str(array[num]), True, (0, 0, 0))
                    self.SCREEN.blit(number, (self.NUMBER_X + h_spacing, self.NUMBER_Y + v_spacing))

                    h_spacing += self.SUBSQUARE_SIZE

                    if num == 8:
                        h_spacing = 0
                        v_spacing += self.SUBSQUARE_SIZE

                # Add randomly generated numbers.
                else:
                    number = number_font.render('', True, (0, 0, 0))
                    self.SCREEN.blit(number, (self.NUMBER_X + h_spacing, self.NUMBER_Y + v_spacing))

                    h_spacing += self.SUBSQUARE_SIZE

                    if num == 8:
                        h_spacing = 0
                        v_spacing += self.SUBSQUARE_SIZE

        # Check if the board is full.
        count = 0

        for row in board:
            for value in row:
                if value > 0:
                    count += 1

        if count == 81:
            return True

    def menu(self):
        """Draws the menu at the bottom of the screen."""

        # Sets a font instance for every menu button.
        font = pygame.font.Font(self.MENU_FONT, self.MENU_FONT_SIZE)
        restart_button = font.render('Restart', True, self.MENU_FONT_COLOR)
        reset_button = font.render('Reset', True, self.MENU_FONT_COLOR)
        exit_button = font.render('Exit', True, self.MENU_FONT_COLOR)

        margin = 179

        # Draws the restart button.
        restart_button_info = (self.BUTTON_X, self.BUTTON_Y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        pygame.draw.rect(self.SCREEN, self.RESTART_COLOR, restart_button_info)
        pygame.draw.rect(self.SCREEN, self.RESTART_BORDER_COLOR, restart_button_info, width=self.BUTTON_BORDER_WIDTH)

        # Draws the reset button.
        reset_button_info = ((self.BUTTON_X * 2) + margin, self.BUTTON_Y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        pygame.draw.rect(self.SCREEN, self.RESET_COLOR, reset_button_info)
        pygame.draw.rect(self.SCREEN, self.RESET_BORDER_COLOR, reset_button_info, width=self.BUTTON_BORDER_WIDTH)

        # Draws the exit button.
        exit_button_info = ((self.BUTTON_X * 3) + (margin * 2), self.BUTTON_Y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        pygame.draw.rect(self.SCREEN, self.EXIT_COLOR, exit_button_info)
        pygame.draw.rect(self.SCREEN, self.EXIT_BORDER_COLOR, exit_button_info, width=self.BUTTON_BORDER_WIDTH)

        # Blit all "restart", "reset", and "exit" to the screen.
        self.SCREEN.blit(restart_button, (self.BUTTON_X + 12, self.BUTTON_Y + 20))
        self.SCREEN.blit(reset_button, ((self.BUTTON_X * 7) + 6, self.BUTTON_Y + 20))
        self.SCREEN.blit(exit_button, ((self.BUTTON_X * 13), self.BUTTON_Y + 20))

        # Get cursor x and y coordinates.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Get click state
        mouse_click = pygame.mouse.get_pressed()

        # Change the color of the restart button if the cursor hovers over it.
        if mouse_x in range(self.BUTTON_X, self.BUTTON_X + self.BUTTON_WIDTH) and mouse_y in range(self.BUTTON_Y, self.BUTTON_Y + self.BUTTON_HEIGHT):
            self.RESTART_COLOR = (0, 204, 102)

            # Return to the starting screen.
            # Change the color again if the restart button is clicked.
            if mouse_click[0]:
                self.RESTART_COLOR = (0, 145, 73)
                start_main()
                return [True, 'restart']

        else:
            self.RESTART_COLOR = (51, 255, 153)

        # Change the color of the reset button if the cursor hovers over it.
        if (mouse_x in range((self.BUTTON_X * 2) + margin, ((self.BUTTON_X * 2) + margin) + self.BUTTON_WIDTH)
                and mouse_y in range(self.BUTTON_Y, self.BUTTON_Y + self.BUTTON_HEIGHT)):
            self.RESET_COLOR = (0, 204, 102)

            # Resets the board by removing all user-inputted numbers.
            # Change the color again if the reset button is clicked.
            if mouse_click[0]:
                self.MOVE_SFX_VOL = 0
                self.RESET_SFX.set_volume(self.RESET_SFX_VOL)
                self.RESET_SFX.play()
                self.RESET_COLOR = (0, 145, 73)

                return [True, 'reset']

        else:
            self.RESET_COLOR = (51, 255, 153)

        # Change the color of the exit button if the cursor hovers over it.
        if (mouse_x in range((self.BUTTON_X * 3) + (margin * 2), ((self.BUTTON_X * 3) + (margin * 2)) + self.BUTTON_WIDTH)
                and mouse_y in range(self.BUTTON_Y, self.BUTTON_Y + self.BUTTON_HEIGHT)):
            self.EXIT_COLOR = (0, 204, 102)

            # Change the color again if the exit button is clicked.
            if mouse_click[0]:
                self.EXIT_COLOR = (0, 145, 73)
                sys.exit()

        else:
            self.EXIT_COLOR = (51, 255, 153)

        self.MOVE_SFX_VOL = 0.4

        return [False]

    def select(self):
        """Sets up the movement keybinds."""

        # Draws the select box.
        select_info = (self.SELECT_X, self.SELECT_Y, self.SELECT_WIDTH, self.SELECT_HEIGHT)
        pygame.draw.rect(self.SCREEN, self.SELECT_COLOR, select_info, width=self.SELECT_BORDER_WIDTH)

        key_pressed = pygame.key.get_pressed()
        self.MOVE_SFX.set_volume(self.MOVE_SFX_VOL)

        # Move the select box up if the up-arrow key is pressed.
        if key_pressed[pygame.K_UP] and self.SELECT_Y > 0:
            self.SELECT_Y -= self.SUBSQUARE_SIZE
            self.MOVE_SFX.play()

        # Move the select box down if the down-arrow key is pressed.
        if key_pressed[pygame.K_DOWN] and self.SELECT_Y < self.HEIGHT - self.SELECT_HEIGHT - 150:
            self.SELECT_Y += self.SUBSQUARE_SIZE
            self.MOVE_SFX.play()

        # Move the select box left if the left-arrow key is pressed.
        if key_pressed[pygame.K_LEFT] and self.SELECT_X > 0:
            self.SELECT_X -= self.SUBSQUARE_SIZE
            self.MOVE_SFX.play()

        # Move the select box right if the right-arrow key is pressed.
        if key_pressed[pygame.K_RIGHT] and self.SELECT_X < self.WIDTH - 100:
            self.SELECT_X += self.SUBSQUARE_SIZE
            self.MOVE_SFX.play()

    def click(self):
        """Sets up the rules of what the user can do with
        their mouse."""

        # Get the location of the mouse on the board.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        self.MOVE_SFX.set_volume(self.MOVE_SFX_VOL)

        # The position of the mouse in rows and columns.
        mouse_row = (mouse_x // self.SUBSQUARE_SIZE) + 1
        mouse_col = (mouse_y // self.SUBSQUARE_SIZE) + 1
        # mouse_box = [mouse_row, mouse_col]

        # Does not allow the select box to go into the menu section.
        if mouse_row in range(1, 10) and mouse_col in range(1, 10) and mouse_click[0]:
            self.SELECT_X = (mouse_row * self.SUBSQUARE_SIZE) - self.SUBSQUARE_SIZE
            self.SELECT_Y = (mouse_col * self.SUBSQUARE_SIZE) - self.SUBSQUARE_SIZE
            self.MOVE_SFX.play()
