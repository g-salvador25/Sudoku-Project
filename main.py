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


        self.selected = False
    def set_cell_value(self, value):
        self.value = value

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
            text_rect = text.get_rect(center=(cell_x+60//2, cell_y+60//2))
            self.screen.blit(text, text_rect)



class Board:

    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.board = generate_sudoku(9, 30)
        self.cells = [[Cell(self.board[row][col], row, col, 0, screen) for col in range(9)]for row in range(9)]
        self.selected_cell = None



    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()

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

    def select(self, row, col):
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x, y):
        row =  y//60
        col = x//60
        if 0 <= row < 9 and 0 <= col < 9:
            return row, col
        else:
            return None


    def clear(self):
        if self.selected_cell and self.selected_cell.value != 0:
            self.selected_cell.value = 0


    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.sketched_value = value
        """Sets the sketched value of the current selected cell equal to user entered value.
It will be displayed at the top left corner of the cell using the draw() function"""

    def place_number(self, value):
        if self.selected_cell:
            if self.selected_cell.value == 0 and 1 <= value <= 9:
                self.selected_cell.value = value
        """Sets the value of the current selected cell equal to user entered value.
Called when the user presses the Enter key."""
    def reset_to_original(self):
        for row in self.board:
            for cell in row:
                cell.value = 0
        """Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)"""
    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
        """Returns a Boolean value indicating whether the board is full or not."""

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j].value == 0:
                    return i, j
        return None
        """Finds an empty cell and returns its row and col as a tuple (x, y)."""


    def check_board(self):
        for row in range(self.height):
            for col in range(self.width):
                number = self.cells[row][col].get_value()
                if number != 0 and not SudokuGenerator.is_valid(self, row, col, number):
                    return False
        return True
        """Check whether the Sudoku board is solved correctly."""
