import pygame, sys

from sudoku_generator import *
from board import *


pygame.init()


class Start:
    def __init__(self):
        # Screen settings
        self.COLOR = (0, 255, 128)
        self.START_WIDTH = 600
        self.START_HEIGHT = 600
        self.START_SCREEN = pygame.display.set_mode((self.START_WIDTH, self.START_HEIGHT))
        pygame.display.set_caption('Sudoku | START')

        # Sound settings
        self.MUSIC_VOL = 0.2
        pygame.mixer.music.load('music/start-bg-music.mp3')
        pygame.mixer.music.play(3)
        pygame.mixer.music.set_volume(self.MUSIC_VOL)

        # General letter font settings
        self.FONT = 'fonts/MotleyForcesRegular.ttf'
        self.FONT_COLOR = (255, 255, 255)
        self.BUTTON_FONT_SIZE = 60

        # Main title settings
        self.TITLE_FONT_SIZE = 120
        self.TITLE_FONT_COLOR = (255, 255, 255)
        self.TITLE_POS = (90, 80)

        # Choose difficulty message settings.
        self.DIF_FONT = 30
        self.DIF_COLOR = (255, 255, 255)
        self.DIF_POS = (170, 240)

        # Easy button settings
        self.EASY_COLOR = (153, 255, 204)
        self.EASY_WIDTH = 200
        self.EASY_HEIGHT = 100
        self.EASY_X = 60
        self.EASY_Y = 290

        # Medium button settings
        self.MEDIUM_COLOR = (153, 255, 204)
        self.MEDIUM_WIDTH = 200
        self.MEDIUM_HEIGHT = 100
        self.MEDIUM_X = 310
        self.MEDIUM_Y = 290

        # Hard button settings
        self.HARD_COLOR = (153, 255, 204)
        self.HARD_WIDTH = 200
        self.HARD_HEIGHT = 100
        self.HARD_X = (self.START_WIDTH / 2) - (self.HARD_WIDTH / 2)
        self.HARD_Y = 420

    def title(self):
        """Draws the main title of the game."""

        self.START_SCREEN.fill(self.COLOR)

        font = pygame.font.Font(self.FONT, self.TITLE_FONT_SIZE)
        title = font.render('Sudoku', True, self.TITLE_FONT_COLOR)
        self.START_SCREEN.blit(title, self.TITLE_POS)

    def buttons(self):
        """Draws the start button."""

        choose_dif_font = pygame.font.Font(self.FONT, 30)
        choose_dif = choose_dif_font.render('Choose difficulty:', True, self.FONT_COLOR)
        self.START_SCREEN.blit(choose_dif, self.DIF_POS)

        # Sets a font instance for every button.
        font = pygame.font.Font(self.FONT, self.BUTTON_FONT_SIZE)
        easy_button = font.render('Easy', True, self.FONT_COLOR)
        medium_button = font.render('Medium', True, self.FONT_COLOR)
        hard_button = font.render('Hard', True, self.FONT_COLOR)

        # Draws the easy button.
        easy_button_info = (self.EASY_X, self.EASY_Y, self.EASY_WIDTH, self.EASY_HEIGHT)
        pygame.draw.rect(self.START_SCREEN, self.EASY_COLOR, easy_button_info)

        # Draws the medium button.
        medium_button_info = (self.MEDIUM_X - 20, self.MEDIUM_Y, self.MEDIUM_WIDTH + 40, self.MEDIUM_HEIGHT)
        pygame.draw.rect(self.START_SCREEN, self.MEDIUM_COLOR, medium_button_info)

        # Draws the hard button.
        hard_button_info = (self.HARD_X, self.HARD_Y, self.HARD_WIDTH, self.HARD_HEIGHT)
        pygame.draw.rect(self.START_SCREEN, self.HARD_COLOR, hard_button_info)

        # Blits both buttons to the screen.
        self.START_SCREEN.blit(easy_button, ((self.EASY_X + 35), (self.EASY_Y + 25)))
        self.START_SCREEN.blit(medium_button, ((self.MEDIUM_X - 3), (self.MEDIUM_Y + 25)))
        self.START_SCREEN.blit(hard_button, ((self.HARD_X + 35), (self.HARD_Y + 25)))

        # Get the location of the mouse on the screen.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Change the color of the easy button if the cursor hovers over it.
        if (mouse_x in range(int(self.EASY_X), int(self.EASY_X + self.EASY_WIDTH))
                and mouse_y in range(self.EASY_Y, self.EASY_Y + self.EASY_HEIGHT)):
            self.EASY_COLOR = (0, 204, 102)

            if mouse_click[0]:
                # Change the color again if the easy button is clicked.
                # Return true to start the game loop.
                self.EASY_COLOR = (0, 145, 73)
                return True

        else:
            self.EASY_COLOR = (153, 255, 204)

        # Change the color of the medium button if the cursor hovers over it.
        if (mouse_x in range(int(self.MEDIUM_X), int(self.MEDIUM_X + self.MEDIUM_WIDTH))
                and mouse_y in range(self.MEDIUM_Y, self.MEDIUM_Y + self.MEDIUM_HEIGHT)):
            self.MEDIUM_COLOR = (0, 204, 102)

            # Change the color again if the medium button is clicked.
            if mouse_click[0]:
                self.MEDIUM_COLOR = (0, 145, 73)
                return True

        else:
            self.MEDIUM_COLOR = (153, 255, 204)

        # Change the color of the hard button if the cursor hovers over it.
        if (mouse_x in range(int(self.HARD_X), int(self.HARD_X + self.HARD_WIDTH))
                and mouse_y in range(self.HARD_Y, self.HARD_Y + self.HARD_HEIGHT)):
            self.HARD_COLOR = (0, 204, 102)

            if mouse_click[0]:
                # Change the color again if the hard button is clicked.
                # Return true to start the game loop.
                self.HARD_COLOR = (0, 145, 73)
                return True

        else:
            self.HARD_COLOR = (153, 255, 204)


class Won:
    def __init__(self):
        # Screen settings
        self.COLOR = (0, 255, 128)
        self.WIN_WIDTH = 600
        self.WIN_HEIGHT = 600
        self.WIN_SCREEN = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))

        # Sound settings
        self.MUSIC_VOL = 0.2
        pygame.mixer.music.load('music/win-bg-music.mp3')
        pygame.mixer.music.play(3)
        pygame.mixer.music.set_volume(self.MUSIC_VOL)

        # General letter font settings
        self.FONT = 'fonts/MotleyForcesRegular.ttf'
        self.FONT_COLOR = (255, 255, 255)

        # Winning message settings
        self.WIN_FONT_SIZE = 60
        self.WIN_POS = (100, 80)

        # Exit button settings
        self.EXIT_COLOR = (153, 255, 204)
        self.EXIT_WIDTH = 180
        self.EXIT_HEIGHT = 90
        self.EXIT_X = (self.WIN_WIDTH / 2) - (self.EXIT_WIDTH / 2)
        self.EXIT_Y = 260
        self.EXIT_FONT_SIZE = 60

    def win_message(self):
        """Draws the winning message."""

        self.WIN_SCREEN.fill(self.COLOR)

        font = pygame.font.Font(self.FONT, self.WIN_FONT_SIZE)
        win_message = font.render('Hey! You won!', True, self.FONT_COLOR)
        self.WIN_SCREEN.blit(win_message, self.WIN_POS)

    def exit_button(self):
        """Draws the exit button."""

        # Sets a font instance for the exit button.
        font = pygame.font.Font(self.FONT, self.EXIT_FONT_SIZE)
        exit_button = font.render('Exit', True, self.FONT_COLOR)

        # Draws the exit button.
        exit_button_info = (self.EXIT_X, self.EXIT_Y, self.EXIT_WIDTH, self.EXIT_HEIGHT)
        pygame.draw.rect(self.WIN_SCREEN, self.EXIT_COLOR, exit_button_info)

        # Blits the exit button to the screen.
        self.WIN_SCREEN.blit(exit_button, ((self.EXIT_X + 36), (self.EXIT_Y + 23)))

        # Get the location of the mouse on the screen.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Change the color of the exit button if the cursor hovers over it.
        if (mouse_x in range(int(self.EXIT_X), int(self.EXIT_X + self.EXIT_WIDTH))
                and mouse_y in range(self.EXIT_Y, self.EXIT_Y + self.EXIT_HEIGHT)):
            self.EXIT_COLOR = (0, 204, 102)

            if mouse_click[0]:
                # Change the color again if the exit button is clicked.
                # Return true to start the game loop.
                self.EXIT_COLOR = (0, 145, 73)
                sys.exit()

        else:
            self.EXIT_COLOR = (153, 255, 204)


if __name__ == '__main__':
    # Start menu main loop
    start = Start()

    while True:
        clock = pygame.time.Clock()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        start.title()

        if start.buttons():
            pygame.mixer.music.stop()
            break

        pygame.display.update()
        clock.tick(60)

    # Game main loop
    board = Board()

    while True:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        board.draw()
        board.menu()
        board.select()
        board.click()

        pygame.display.update()
        board.SCREEN.fill(board.COLOR)
        clock.tick(12)

    # This code is unreachable unitl we've implemented the RNG.
    win = Won()

    while True:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        win.win_message()
        win.exit_button()

        pygame.display.update()
        clock.tick(60)
