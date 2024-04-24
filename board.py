import random, math, pygame


class Board:
    pygame.init()

    def __init__(self, difficulty='easy'):
        # Screen settings
        self.COLOR = (255, 255, 255)
        self.WIDTH = 660
        self.HEIGHT = 780
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Sudoku')

        # Square settings
        self.SQUARE_SIZE = 220
        self.SUBSQUARE_SIZE = 73
        self.ROWS = 3
        self.COLS = 3
        self.LINE_COLOR = (0, 0, 0)
        self.SUBLINE_COLOR = (64, 64, 64)
        self.LINE_WIDTH = 6
        self.SUBlINE_WIDTH = 2

        # Select box settings
        self.SELECT_COLOR = (255, 0, 0)
        self.SELECT_LEFT = 0
        self.SELECT_TOP = 0
        self.SELECT_WIDTH = 73
        self.SELECT_HEIGHT = 73
        self.SELECT_BORDER_WIDTH = 2

        # Game difficulty
        self.difficulty = difficulty

    def draw(self):
        """Draws an outline of the Sudoku grid, with bold
        lines to delineate the 3x3 boxex. It also draws
        every cell on the board."""

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

    def select(self):
        """Marks the cell at (row, col) in the board
        as the current selected cell. Once a cell has
        been selected, the user can edit its value or
        sketched value."""
        
        # The select box
        select_coords = (self.SELECT_LEFT, self.SELECT_TOP, self.SELECT_WIDTH, self.SELECT_HEIGHT)
        pygame.draw.rect(self.SCREEN, self.SELECT_COLOR, select_coords, width=self.SELECT_BORDER_WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Moves select box up if the up arrow key or the "w" key is pressed.
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.SELECT_TOP -= 73
                
                # Moves the select box down if the down arrow key or the "s" key is pressed.
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.SELECT_TOP += 73
                
                # Moves the select box left if the left arrow key or the "a" key is pressed.
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.SELECT_LEFT -= 73
                
                # Moves the select box right if the right arrow key or the "s" key is pressed.
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.SELECT_LEFT += 73
