import math, random
import pygame
from sudoku_generator import SudokuGenerator, generate_sudoku


class Cell:

    def __init__(self, value, row, col, sketched_value, screen):
        self.value = value
        self.row = row
        self.col = col
        self.sketched_value = sketched_value
        self.screen = screen
        #self.board = generate_sudoku()


        self.selected = False
    def set_cell_value(self, value):
        self.board[self.row][self.col] = value

    def set_sketched_value(self, sketch):
        self.sketched_value = sketch

    def draw(self):
        cell_x = self.col * 60
        cell_y = self.row * 60
        cell_rect = pygame.Rect(cell_x,cell_y, 60, 60)
        pygame.draw.rect(self.screen, (255,255,255), cell_rect)
        if self.selected:
            pygame.draw.rect(self.screen, (255,0,0), cell_rect, 3)
        if self.value != 0:
            font = pygame.font.Font(None, 60)
            text = font.render(str(self.value), True, (0,0,0))
            text_rect = text.get_rect(center=(cell_x+self.cell_size//2, cell_y+self.cell_size//2))
            self.screen.blit(text, text_rect)

    #this is not complete and needs to be done

class Board:

    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.screen = screen
        self.cells
        self.selected_cell = None

    def draw(self):
        for i in range(0, 10):
            if i % 3 == 0:
                width = 7
            else:
                width = 3
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             (0, i * 60),
                             (540, i * 60),
                             width)

        for i in range(0, 10):
            if i % 3 == 0:
                width = 7
            else:
                width = 3
            pygame.draw.line(self.screen,
                             (0, 0, 0),
                             (i * 60, 0),
                             (i * 60, 540),
                             width)
        for row in self.cells

    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value"""

    def click(self, x, y):
        """If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        of the cell which was clicked. Otherwise, this function returns None."""
    def clear(self):
        """Clears the value cell. Note that the user can only remove the cell values and sketched value that are
filled by themselves."""

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to user entered value.
It will be displayed at the top left corner of the cell using the draw() function"""

    def place_number(self, value):
        """Sets the value of the current selected cell equal to user entered value.
Called when the user presses the Enter key."""
    def reset_to_original(self):
        """Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)"""
    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""


    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""
