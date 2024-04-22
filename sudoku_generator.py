import math, random


class SudokuGenerator:
    # creates the sudoku BOARD
    # ROW_LENGTH is always gonna be 9
    # creates 2D array representing the BOARD
    # determines the size of boxes
    def __init__(self, ROW_LENGTH, REMOVED_CELLS):
        self.ROW_LENGTH = ROW_LENGTH
        self.REMOVED_CELLS = REMOVED_CELLS
        self.BOARD = [[0 for x in range(9)] for y in range()]
        self.BOX_LENGTH = math.sqrt(ROW_LENGTH)

    # returns the 2D array representing the BOARD
    def get_board(self):
        return self.BOARD

    # prints the BOARD to console
    def print_board(self):
        for row in self.BOARD:
            print(' '.join(map(str, row)))

    # determiens if value is in a row. It will iterate through that row
    # in the 2D array and return False if the value is in the row
    def valid_in_row(self, row, num):
        for value in self.BOARD[row]:
            if value == num:
                return False
        return True

    # determiens if value is in a column. It will iterate through that column
    # in the 2D array and return False if the value is in the column
    def valid_in_col(self, col, num):
        for row in self.BOARD:
            if row[col] == num:
                return False
        return True

    # determiens if value is in its box. It will iterate through the whole box
    # by using the 2D array and return False if the value is in the box
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start+2):
            for j in range(col_start, col_start+2):
                if self.BOARD[i][j] == num:
                    return False
        return True

    # determines if a value wanting to be entered is valid and necessary based
    # on whether its valid in its row, column, and box by using the previous methods.
    # Depending on the row and column of where the value wants to be entered,
    # we have to find what box grid its in. The following if-statements
    # determine what box grid its in.
    def is_valid(self, row, col, num):
        if row <= 2:
            box_row = 0
        elif row <= 5:
            box_row = 3
        else:
            box_row = 6
        if col <= 2:
            box_col = 0
        elif col <= 5:
            box_col = 3
        else:
            box_col = 6

        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(box_row, box_col, num):
            return True
        return False

    # Fills a desired "box" with values without repeating or duplicating values
    def fill_box(self, row_start, col_start):
        for i in range(row_start, row_start + 2):
            for j in range(col_start, col_start + 2):
                random_value = math.random.randint(1, 9)
                if is_valid(i, j, random_value):
                    self.BOARD[i][j] == random_value

    # Uses the previous fill_box() method three times in order to create the three boxes on the diagonal
    def fill_diagonal(self):
        row_start = 0
        column_start = 0
        for i in range(2):
            fill_box(row_start, column_start)
            row_start += 3
            column_start += 3


    # Given from the instructions. Not to be changed at all.
    def fill_remaining(self, row, col):
        if (col >= self.ROW_LENGTH and row < self.ROW_LENGTH - 1):
            row += 1
            col = 0
        if row >= self.ROW_LENGTH and col >= self.ROW_LENGTH:
            return True
        if row < self.BOX_LENGTH:
            if col < self.BOX_LENGTH:
                col = self.BOX_LENGTH
        elif row < self.ROW_LENGTH - self.BOX_LENGTH:
            if col == int(row // self.BOX_LENGTH * self.BOX_LENGTH):
                col += self.BOX_LENGTH
        else:
            if col == self.ROW_LENGTH - self.BOX_LENGTH:
                row += 1
                col = 0
                if row >= self.ROW_LENGTH:
                    return True

        for num in range(1, self.ROW_LENGTH + 1):
            if self.is_valid(row, col, num):
                self.BOARD[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.BOARD[row][col] = 0
        return False

    # Given from the instructions. Not to be changed at all.
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.BOX_LENGTH)

    # Based on the difficulty, this method makes the board
    # have values already at the start of the game
    def remove_cells(self):
        flat_board = [cell for row in self.BOARD for cell in row]

        for i in range(self.REMOVED_CELLS):
            while True:
                random_index = math.random.randint(0, 80)
                if flat_board[random_index] == 0:
                    continue
                flat_board[random_index] = 0
                break

        self.BOARD = [flat_board[i:i+9] for i in range(0, 81, 9)]

    # Given from the instructions. Not to be changed at all.
    def generate_sudoku(size, removed):
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        BOARD = sudoku.get_board()
        sudoku.remove_cells()
        BOARD = sudoku.get_board()
        return BOARD
