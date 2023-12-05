import math, random
import pygame


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):

    #this is not complete and needs to be done

class Board(Cell):

    def __init__(self, width, height, screen):
        super().__init__(value, row, col, screen)
        self.width = width
        self.height = height
        self.screen = screen

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

    def select(self, row, col):

    def click(self, x, y):

    def clear(self):

    def sketch(self, value):

    def place_number(self, value):

    def reset_to_original(self):

    def is_full(self):

    def update_board(self):

    def find_empty(self):

    def check_board(self):

