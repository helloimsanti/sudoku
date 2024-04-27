import pygame, sys

from sudoku_generator import *
from board import *


pygame.init()


class Start:
    def __init__(self):
        # Screen settings
        self.COLOR = (0, 255, 128)
        self.START_WIDTH = 660
        self.START_HEIGHT = 780
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
        self.TITLE_POS = (120, 80)

        # Choose difficulty message settings.
        self.DIF_FONT = 30
        self.DIF_COLOR = (255, 255, 255)
        self.DIF_POS = (200, 240)

        # Easy button settings
        self.EASY_COLOR = (153, 255, 204)
        self.EASY_WIDTH = 200
        self.EASY_HEIGHT = 100
        self.EASY_X = 100
        self.EASY_Y = 290

        # Medium button settings
        self.MEDIUM_COLOR = (153, 255, 204)
        self.MEDIUM_WIDTH = 200
        self.MEDIUM_HEIGHT = 100
        self.MEDIUM_X = 350
        self.MEDIUM_Y = 290

        # Hard button settings
        self.HARD_COLOR = (153, 255, 204)
        self.HARD_WIDTH = 200
        self.HARD_HEIGHT = 100
        self.HARD_X = (self.START_WIDTH / 2) - (self.HARD_WIDTH / 2)
        self.HARD_Y = 420

        # Author settings
        self.AUTHORS_FONT_SIZE = 20
        self.AUTHORS_POS = (120, 700)

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

        # Blits "easy", "medium", and "hard" to the screen.
        self.START_SCREEN.blit(easy_button, (self.EASY_X + 34, self.EASY_Y + 25))
        self.START_SCREEN.blit(medium_button, (self.MEDIUM_X - 2, self.MEDIUM_Y + 25))
        self.START_SCREEN.blit(hard_button, (self.HARD_X + 35, self.HARD_Y + 25))

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

    def authors(self):
        """Draws the names of the game's authors."""

        message = 'By Santiago A., John B., Giles G., and Joshua R.'
        font = pygame.font.Font(self.FONT, self.AUTHORS_FONT_SIZE)
        authors = font.render(message, True, self.FONT_COLOR)
        self.START_SCREEN.blit(authors, self.AUTHORS_POS)


class Won:
    def __init__(self):
        # Screen settings
        self.COLOR = (0, 255, 128)
        self.WIN_WIDTH = 660
        self.WIN_HEIGHT = 780
        self.WIN_SCREEN = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        pygame.display.set_caption('Sudoku | You won!')

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
        self.WIN_POS = (135, 80)

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

        # Blits "exit" to the screen.
        self.WIN_SCREEN.blit(exit_button, (self.EXIT_X + 36, self.EXIT_Y + 23))

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


class Lose:
    def __init__(self):
        # Screen settings
        self.COLOR = (0, 255, 128)
        self.LOSE_WIDTH = 660
        self.LOSE_HEIGHT = 780
        self.LOSE_SCREEN = pygame.display.set_mode((self.LOSE_WIDTH, self.LOSE_HEIGHT))
        pygame.display.set_caption('Sudoku | You lost')

        # Sound settings
        self.MUSIC_VOL = 0.2
        pygame.mixer.music.load('sfx/lose-sfx.mp3')
        pygame.mixer.music.set_volume(self.MUSIC_VOL)
        pygame.mixer.music.play()

        # General letter font settings
        self.FONT = 'fonts/MotleyForcesRegular.ttf'
        self.FONT_COLOR = (255, 255, 255)

        # Winning message settings
        self.LOSE_FONT_SIZE = 60
        self.LOSE_POS = (205, 80)

        # Exit button settings
        self.RESTART_COLOR = (153, 255, 204)
        self.RESTART_WIDTH = 240
        self.RESTART_HEIGHT = 120
        self.RESTART_X = (self.LOSE_WIDTH / 2) - (self.RESTART_WIDTH / 2)
        self.RESTART_Y = 590
        self.RESTART_FONT_SIZE = 60

    def lose_message(self):
        """Draws the losing message."""

        self.LOSE_SCREEN.fill(self.COLOR)

        font = pygame.font.Font(self.FONT, self.LOSE_FONT_SIZE)
        win_message = font.render('You lost.', True, self.FONT_COLOR)
        self.LOSE_SCREEN.blit(win_message, self.LOSE_POS)

    def restart_button(self):

        # Sets a font instance for the exit button.
        font = pygame.font.Font(self.FONT, self.RESTART_FONT_SIZE)
        restart_button = font.render('Restart', True, self.FONT_COLOR)

        # Draws the restart button.
        restart_button_info = (self.RESTART_X, self.RESTART_Y, self.RESTART_WIDTH, self.RESTART_HEIGHT)
        pygame.draw.rect(self.LOSE_SCREEN, self.RESTART_COLOR, restart_button_info)

        # Blit restart to the screen.
        self.LOSE_SCREEN.blit(restart_button, (self.RESTART_X + 12, self.RESTART_Y + 35))

        # Get the location of the mouse on the screen.
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Change the color of the restart button if the cursor hovers over it.
        if (mouse_x in range(int(self.RESTART_X), int(self.RESTART_X + self.RESTART_WIDTH))
                and mouse_y in range(self.RESTART_Y, self.RESTART_Y + self.RESTART_HEIGHT)):
            self.RESTART_COLOR = (0, 204, 102)

            if mouse_click[0]:
                # Change the color again if the restart button is clicked.
                # Return true to start the game loop.
                self.RESTART_COLOR = (0, 145, 73)
                return True

        else:
            self.RESTART_COLOR = (153, 255, 204)


def game_main():
    """Game main loop"""

    board = Board()

    while True:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        board.draw()

        if board.menu():
            break

        board.select()
        board.click()

        pygame.display.update()
        board.SCREEN.fill(board.COLOR)
        clock.tick(12)


def start_main():
    """Start menu main loop"""

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

        start.authors()

        pygame.display.update()
        clock.tick(60)


def reset_game():
    """Resets the game."""

    start_main()
    game_main()


def win_main():
    """This code is unreachable unitl we've implemented the RNG."""

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


def lose_main():
    """This code is unreachable until we've implemented the RNG."""

    lose = Lose()

    while True:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        lose.lose_message()

        if lose.restart_button():
            reset_game()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    reset_game()
    # win_main()
    # lose_main()
