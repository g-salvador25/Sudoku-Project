import pygame, sys
from sudoku_generator import SudokuGenerator


def draw_grid():
    for i in range(0, 10):
        if i % 3 == 0:
            width = 7
        else:
            width = 3
        pygame.draw.line(screen,
                         (0,0,0),
                         (0, i * 60),
                         (540, i * 60),
                         width)

    for i in range(0, 10):
        if i % 3 == 0:
            width = 7
        else:
            width = 3
        pygame.draw.line(screen,
                         (0,0,0),
                         (i * 60, 0),
                         (i * 60, 540),
                         width)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((540,540))
    screen.fill((255, 255, 245))
    draw_grid()
    board = SudokuGenerator(9,9)
    board.is_valid(9,9)



while True:
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT:
            pygame.quit()





